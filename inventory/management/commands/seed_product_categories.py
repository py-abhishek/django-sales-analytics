from django.core.management.base import BaseCommand
import json

from inventory.models import ProductCategory


class Command(BaseCommand):
    help = 'Create sample products categories'

    with open('inventory/fixtures/product_categories.json', 'r') as f:
        categories = json.load(f)


    def handle(self, *args, **options):
        print(self.categories)

    # {"name": "Power Solutions", "description": "UPS systems, extension boards, surge protectors, and power supplies"}
#   name = models.CharField(max_length=100, unique=True)
#     description = models.TextField(blank=True)
#     business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='product_categories')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

        product_categories = []
        for item in self.categories:
            product_categories.append(ProductCategory(
                name=item.name,
                description=item.description,
                business_id=1
            ))

        ProductCategory.objects.bulk_create(product_categories)
        print("Data Inserted Successfully")
        

        