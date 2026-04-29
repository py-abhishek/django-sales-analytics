from django.db import transaction
from django.core.exceptions import ValidationError
from django.contrib import messages

from .models import Sale, SaleItem
from inventory.services import create_sale_ledger, create_cancel_sale_ledger
from .models import Customer


import logging
logger = logging.getLogger(__name__)

# Validate and create sale
def create_sale(customer_id, is_new_customer, customer_form_data, sale_form_data, formset_data, business_id, user):
    '''
    This function will validate if item available in the stock,
    then deduct it from the stock,
    calcalate totals, profits, 
    and then create sale
    '''

    # remove empty item from formset
    cleaned_formset_data = get_cleaned_formset_data(formset_data)

    with transaction.atomic():
        validate_formset_data(formset_data) # Validate Products
        
        if is_new_customer:
            customer = Customer.objects.create(
                name=customer_form_data['name'],
                phone=customer_form_data['phone'],
                email=customer_form_data['email'],
                address=customer_form_data['address'],
                business_id=business_id
            )
        else:
            customer = Customer.objects.get(id=customer_id)

        sale = Sale.objects.create(
            customer=customer,
            sale_date=sale_form_data['sale_date'],
            total_amount=get_total_sale_amount(cleaned_formset_data),
            total_profit=get_total_profit(cleaned_formset_data),
            payment_method=sale_form_data['payment_method'],
            business_id=business_id,
            created_by=user
            )

        for item in cleaned_formset_data:
            product = item['product']
            quantity = item['quantity']

            SaleItem.objects.create(
                sale=sale,
                product=product,
                quantity=quantity,
                unit=product.unit,
                price_at_sale=product.selling_price,
                cost_at_sale=product.current_avg_cost,
                item_total_price=get_item_total_price(product, item),
                item_profit=get_item_profit(product, item),
                business_id=business_id
            )

            # Updating Stock Ledger
            unit_cost = product.current_avg_cost
            total_cost = (unit_cost * quantity)
            create_sale_ledger(product, quantity, unit_cost, total_cost, sale, business_id)

            deduct_stock(product, item) # Update stock

        return sale
    
def validate_formset_data(formset_data):
    cleaned_formset_data = get_cleaned_formset_data(formset_data)

    if not cleaned_formset_data:
        raise ValidationError('Please Choose a Product')
    
    seen_products = set()
    for item in cleaned_formset_data:
        # check for duplicates
        product_sku = item['product'].sku

        if product_sku in seen_products:
            print("error")
            raise ValidationError('This product is already in the list. Update the quantity instead.')
        seen_products.add(product_sku)

        if not available_in_stock(item['product'], item):
            raise ValidationError(
                f'Insufficient stock for {item['product'].name}. '
                f'Available: {item['product'].current_stock}, '
                f'Requested: {item['quantity']}.'
            )
    
def get_cleaned_formset_data(formset_data):
    return [
        item for item in formset_data
        if item
        and not item.get('delete')
        and item.get('product')
        # and item.get('unit')
        and item.get('quantity') is not None 
    ]


# Check product availability
def available_in_stock(product, item):
    current_stock = product.current_stock
    return current_stock >= item['quantity']


# Update product quantity
def deduct_stock(product, item):
    # c_current_stock = product.current_stock
    sale_quantity = item['quantity']
    product.current_stock -= sale_quantity
    product.save()


def get_item_total_price(product, item):
    return product.selling_price * item['quantity']


def get_item_profit(product, item):
    return (product.selling_price - product.current_avg_cost) * item['quantity']


def get_total_sale_amount(clean_formset_data):
    total = 0
    for item in clean_formset_data:
        total += get_item_total_price(item['product'], item)
    return total


def get_total_profit(clean_formset_data):
    profit = 0
    for item in clean_formset_data:
        profit += get_item_profit(item['product'], item)
    return profit


# Cancel a sale
def cancel_sale(request, sale_id, business_id):
    sale = Sale.objects.get(business_id=business_id, id=sale_id)
    if sale.is_cancelled():
        messages.info(request, 'This sale is already cancelled')
        return
    
    # Reverse stock
    for item in sale.items.all():
        product = item.product
        product.current_stock += item.quantity
        product.save()

        # Update inventory ledger
        create_cancel_sale_ledger(business_id, sale, product, item.quantity, item.cost_at_sale)

    sale.status = Sale.StatusChoices.CANCELLED
    sale.save()

    messages.success(request, 'Sale cancelled successfully.')
