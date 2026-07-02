from django.core.management.base import BaseCommand
import json

from inventory.models import ProductCategory
from .seed_utils import get_or_create_membership
from core.seeders import seed_products, seed_product_categories, seed_customers, seed_sales, seed_expenses, seed_purchases, seed_expense_categories, seed_suppliers


class Command(BaseCommand):
    help = 'Create sample data'
    
    business_name = 'TechZone Electronics'
    membership = get_or_create_membership(business_name)
    user = membership.user
    business = membership.business

    suppliers_data = 'core/fixtures/suppliers.json'
    customers_data = 'core/fixtures/customers.json'
    exp_categories_data = 'core/fixtures/expense_categories.json'
    exp_data = 'core/fixtures/expenses.json'
    product_categories_data = 'core/fixtures/product_categories.json'
    products_data = 'core/fixtures/products.json'


    def handle(self, *args, **options):
        print('Inserting product categories...')
        seed_product_categories.seed_product_categories(self.product_categories_data, self.business)
        print('Product categories inserted successfully')


        print('Inserting products...')
        seed_products.seed_products(self.products_data, self.business, self.user)
        print('Products inserted successfully')


        print('Inserting suppliers...')
        seed_suppliers.seed_suppliers(self.suppliers_data, self.business)
        print('Suppliers inserted successfully')


        print('Inserting purchases...')
        seed_purchases.seed_purchases(self.business, 200)
        print('Purchases added successfully')


        print('Inserting customers...')
        seed_customers.seed_customers(self.customers_data, self.business)
        print('Customers inserted successfully')


        print('Inserting sales...')
        seed_sales.seed_sales(self.business, self.user, 500)
        print('Sales created successfully')


        print('Inserting expense categories...')
        seed_expense_categories.seed_expense_categories(self.exp_categories_data, self.business)
        print('Expese categories created successfully')


        print('Inserting expenses...')
        seed_expenses.seed_expenses(self.exp_data, self.business, self.user)
        print('Expenses added successfully')