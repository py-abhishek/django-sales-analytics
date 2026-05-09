
import random
from django.utils import timezone
from datetime import timedelta

from inventory.models import Product
from purchases.models import Supplier, Purchase
from purchases import services


def seed_purchases(business):

    purchase_form_data = {}
    supplier_form_data = {}

    for i in range(219):
        supplier_id = random.choice(Supplier.objects.all()).id
        purchase_form_data['payment_method'] = random.choice(Purchase._meta.get_field('payment_method').choices)[0]
        purchase_form_data['purchase_date'] = get_random_date()
        formset_data = []

        products = Product.objects.all()

        for j in range(random.randint(1, 10)):

            
            is_duplicate = False
            product = random.choice(products)
            for item in formset_data:
                if product == item['product']:
                    is_duplicate = True
                    break

            if is_duplicate: 
                continue # Return if product already in the list
            
            
            formset_data.append({
                'product': product,
                'quantity': random.randint(1,4),
                'unit_cost': product.current_avg_cost + random.randint(-100, 100)
                })
        
        try:
            services.create_purchase(
                supplier_id=supplier_id,
                is_new_supplier=False, 
                supplier_form_data=supplier_form_data,
                purchase_form_data=purchase_form_data,
                formset_data=formset_data,
                business_id=business.id,
                )
        except Exception as e:
            print(e)
            continue


def get_random_date():
    today = timezone.now().date()
    start_date = today - timedelta(days=365)
    random_days = random.randint(0, 365)
    random_date = start_date + timedelta(days=random_days)
    return random_date