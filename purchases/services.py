from django.db import transaction
from django.core.exceptions import ValidationError

from .models import Purchase, PurchaseItem, Supplier
from inventory.services import create_purchase_ledger, calc_new_avg_cost

import logging
logger = logging.getLogger(__name__)

# Validate data and create purchase
def create_purchase(supplier_id, is_new_supplier, supplier_form_data, purchase_form_data, formset_data, business_id):

    # remove empty item from formset
    cleaned_formset_data = get_cleaned_formset_data(formset_data)


    with transaction.atomic():
        validate_formset_data(formset_data) # Validate Products
        
        if is_new_supplier:
            supplier = Supplier.objects.create(
                name=supplier_form_data['name'],
                phone=supplier_form_data['phone'],
                email=supplier_form_data['email'],
                address=supplier_form_data['address'],
                business_id=business_id
            )
        else:
            supplier = Supplier.objects.get(id=supplier_id)

        purchase = Purchase.objects.create(
            supplier=supplier,
            purchase_date=purchase_form_data['purchase_date'],
            total_amount=get_total_purchase_amount(cleaned_formset_data),
            payment_method=purchase_form_data['payment_method'],
            business_id=business_id
            )

        for item in cleaned_formset_data:
            product = item['product']
            quantity = item['quantity']
            unit_cost = item['unit_cost']
            total_cost = get_item_total_cost(item)

            PurchaseItem.objects.create(
                purchase=purchase,
                product=product,
                quantity=item['quantity'],
                unit=product.unit,
                unit_cost=item['unit_cost'],
                item_total_cost=total_cost,
                business_id=business_id
            )

            create_purchase_ledger(product, item['quantity'], unit_cost, total_cost, purchase, business_id) # recording ledger for history
            update_stock(product, item) # increase stock and update avg cost of purchased products
            

        return purchase
    
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

    
def get_cleaned_formset_data(formset_data):
    return [
        item for item in formset_data
        if item
        and not item.get('delete')
        and item.get('product')
        and item.get('unit_cost')
        and item.get('quantity') is not None 
    ]


# Update product stock cost and quantity
def update_stock(product, item):
    # Update stock quantity
    # c_current_stock = product.current_stock
    purchase_quantity = item['quantity']
    product.current_stock += purchase_quantity

    # Update average cost
    new_qty = item['quantity']
    new_cost = item['unit_cost']
    new_avg_cost = calc_new_avg_cost(product, new_qty, new_cost)
    product.current_avg_cost = new_avg_cost

    product.save()


def get_item_total_cost(item):
    return item['unit_cost'] * item['quantity']


def get_total_purchase_amount(cleaned_formset_data):
    total = 0
    for item in cleaned_formset_data:
        total += get_item_total_cost(item)
    return total



