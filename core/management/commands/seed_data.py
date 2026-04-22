from django.core.management.base import BaseCommand
import json

from inventory.models import ProductCategory
from .seed_utils import get_or_create_membership
from core.seeders.inventory import seed_product_categories, seed_products


class Command(BaseCommand):
    help = 'Create sample data'
    
    membership = get_or_create_membership()
    user = membership.user
    business = membership.business


    def handle(self, *args, **options):
        # seed_product_categories.seed_product_categories(self.business)
        # print("Product categories inserted successfully")


        seed_products.seed_products(self.business, self.user)
        print("Products inserted successfully")


        

        