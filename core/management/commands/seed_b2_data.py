from django.core.management.base import BaseCommand
import json

from inventory.models import ProductCategory
from .seed_utils import get_or_create_membership
from core.seeders import seed_products, seed_product_categories, seed_customers, seed_sales, seed_expenses, seed_purchases, seed_expense_categories, seed_suppliers


class Command(BaseCommand):
    help = 'Create sample data'
    
    
    business_name = 'FreshMart Grocery'
    membership = get_or_create_membership(business_name)
    user = membership.user
    business = membership.business

    suppliers_data = 'core/fixtures/suppliers_02.json'
    customers_data = 'core/fixtures/customers_02.json'
    exp_categories_data = 'core/fixtures/expense_categories_02.json'
    exp_data = 'core/fixtures/expenses_02.json'
    product_categories_data = 'core/fixtures/product_categories_02.json'
    products_data = 'core/fixtures/products_02.json'


    def handle(self, *args, **options):
        seed_product_categories.seed_product_categories(self.product_categories_data, self.business)
        print('Product categories inserted successfully')


        seed_products.seed_products(self.products_data, self.business, self.user)
        print('Products inserted successfully')

        seed_suppliers.seed_suppliers(self.suppliers_data, self.business)
        print('Suppliers inserted successfully')

        seed_purchases.seed_purchases(self.business, 500)
        print('Purchases added successfully')

        seed_customers.seed_customers(self.customers_data, self.business)
        print('Customers inserted successfully')

        seed_sales.seed_sales(self.business, self.user, 2000)
        print('Sales created successfully')

        seed_expense_categories.seed_expense_categories(self.exp_categories_data, self.business)
        print('Expese categories created successfully')

        seed_expenses.seed_expenses(self.exp_data, self.business, self.user)
        print('Expenses created added successfully')



        

        