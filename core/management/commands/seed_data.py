from django.core.management.base import BaseCommand
import json

from inventory.models import ProductCategory
from .seed_utils import get_or_create_membership
from core.seeders import seed_products, seed_product_categories, seed_customers, seed_sales, seed_expenses, seed_purchases, seed_expense_categories, seed_suppliers


class Command(BaseCommand):
    help = 'Create sample data'
    
    membership = get_or_create_membership()
    user = membership.user
    business = membership.business


    def handle(self, *args, **options):
        # seed_product_categories.seed_product_categories(self.business)
        # print('Product categories inserted successfully')


        # seed_products.seed_products(self.business, self.user)
        # print('Products inserted successfully')

        # seed_suppliers.seed_suppliers(self.business)
        # print('Suppliers inserted successfully')

        seed_purchases.seed_purchases(self.business)
        print('Purchases added successfully')

        # seed_customers.seed_customers(self.business)
        # print('Customers inserted successfully')

        # seed_sales.seed_sales(self.business, self.user)
        # print('Sales created successfully')

        # seed_expense_categories.seed_expense_categories(self.business)
        # print('Expese categories created successfully')

        # seed_expenses.seed_expenses(self.business, self.user)
        # print('Expenses created added successfully')



        

        