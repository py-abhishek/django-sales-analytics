from django.core.management.base import BaseCommand
from sales.views.models.models import Customer


class Command(BaseCommand):
    help = 'Create sample customers'

    customer_list = []

    customers = []

    def handle(self, *args, **options):
        for c in self.customer_list:
            self.customers.append(Customer(**c))

        Customer.objects.bulk_create(self.customers)

        print('Customers added successfully')

        