from django.core.management.base import BaseCommand
from inventory.models import Product, ProductCategory


class Command(BaseCommand):
    help = 'Create sample products'

    product_list = [

    ]


    products = []

    def handle(self, *args, **options):

        for item in self.product_list:
            product = Product(
                name = item['name'],
                description = item['description'],
                sku = item['sku'],
                category = ProductCategory.objects.get(name=item['category']),
                current_avg_cost = item['cost_price'],
                selling_price = item['selling_price'],
                current_stock = item['stock_quantity'],
                unit = item['unit'],
                reorder_level = item['reorder_level']
                )
            
            self.products.append(product)

        Product.objects.bulk_create(self.products)
        print("Producted added successfully")

        