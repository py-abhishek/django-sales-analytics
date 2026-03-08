from django.core.management.base import BaseCommand
import random
from django.utils import timezone
from datetime import timedelta

from inventory.models import Product
from sales.models import Customer, Sale
from sales import services


import random

class Command(BaseCommand):
    help = 'Create sample sales'

    def get_random_date(self):
        today = timezone.now().date()
        start_date = today - timedelta(days=365)
        random_days = random.randint(0, 365)
        random_date = start_date + timedelta(days=random_days)
        return random_date


    def handle(self, *args, **options):

        for i in range(500):

            customer = random.choice(Customer.objects.all())
            p_method = random.choice(Sale._meta.get_field('payment_method').choices)[0]
            date = self.get_random_date()
            products_data = []

            for j in range(random.randint(1, 10)):
                products_data.append({
                    'product': random.choice(Product.objects.all()),
                    'quantity': random.randint(1,4)
                    })
            
            try:
                services.create_sale(customer, date, p_method, products_data)
            except Exception as e:
                print(e)
                continue

        print('Sales created successfully')

        