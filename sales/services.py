from django.db import transaction
from .models import Sale, SaleItem, Customer
from inventory.models import Product
from django.core.exceptions import ValidationError

import logging
logger = logging.getLogger(__name__)

def create_sale(customer_id, is_new_customer, customer_form_data, sale_form_data, formset_data):
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
                address=customer_form_data['address']
            )
        else:
            customer = Customer.objects.get(id=customer_id)

        sale = Sale.objects.create(
            customer=customer,
            sale_date=sale_form_data['sale_date'],
            total_amount=get_total_sale_amount(cleaned_formset_data),
            total_profit=get_total_profit(cleaned_formset_data),
            payment_method=sale_form_data['payment_method']
            )

        for item in cleaned_formset_data:
            product = item['product']
            SaleItem.objects.create(
                sale=sale,
                product=product,
                quantity=item['quantity'],
                unit=product.unit,
                price_at_sale=product.selling_price,
                cost_at_sale=product.cost_price,
                item_total_price=get_item_total_price(product, item),
                item_profit=get_item_profit(product, item)
            )
            
            deduct_stock(product, item)

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
                f'Available: {item['product'].stock_quantity}, '
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


def available_in_stock(product, item):
    stock_quantity = product.stock_quantity
    return stock_quantity >= item['quantity']


def deduct_stock(product, item):
    c_stock_quantity = product.stock_quantity
    sale_quantity = item['quantity']
    product.stock_quantity = c_stock_quantity - sale_quantity
    product.save()


def get_item_total_price(product, item):
    return product.selling_price * item['quantity']


def get_item_profit(product, item):
    return (product.selling_price - product.cost_price) * item['quantity']


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



