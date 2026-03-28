from django.db import transaction
from django.core.exceptions import ValidationError

from .models import Purchase, PurchaseItem, Supplier
from inventory.services import create_purchase_ledger

import logging
logger = logging.getLogger(__name__)

def create_purchase(supplier_id, is_new_supplier, supplier_form_data, purchase_form_data, formset_data):

    # remove empty item from formset
    cleaned_formset_data = get_cleaned_formset_data(formset_data)


    with transaction.atomic():
        validate_formset_data(formset_data) # Validate Products
        
        if is_new_supplier:
            supplier = Supplier.objects.create(
                name=supplier_form_data['name'],
                phone=supplier_form_data['phone'],
                email=supplier_form_data['email'],
                address=supplier_form_data['address']
            )
        else:
            supplier = Supplier.objects.get(id=supplier_id)

        purchase = Purchase.objects.create(
            supplier=supplier,
            purchase_date=purchase_form_data['purchase_date'],
            total_amount=get_total_purchase_amount(cleaned_formset_data),
            payment_method=purchase_form_data['payment_method']
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
                item_total_cost=total_cost
            )

            add_stock(product, item) # increase stock of purchased products
            create_purchase_ledger(product, item['quantity'], unit_cost, total_cost, purchase) # recording ledger for history
            

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



def add_stock(product, item):
    # add stock instead
    c_stock_quantity = product.stock_quantity
    sale_quantity = item['quantity']
    product.stock_quantity = c_stock_quantity + sale_quantity
    product.save()


def get_item_total_cost(item):
    return item['unit_cost'] * item['quantity']


def get_total_purchase_amount(cleaned_formset_data):
    total = 0
    for item in cleaned_formset_data:
        total += get_item_total_cost(item)
    return total



