import json
from inventory.models import ProductCategory

def seed_product_categories(business):

    with open('core/fixtures/product_categories.json', 'r') as f:
        categories = json.load(f)


    product_categories = []
    for item in categories:
        product_categories.append(ProductCategory(
            name=item['name'],
            description=item['description'],
            business=business
        ))

    ProductCategory.objects.bulk_create(product_categories)
        

        