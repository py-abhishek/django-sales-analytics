import json

from inventory.models import ProductCategory, Product

def seed_products(business, user):
    with open('core/fixtures/inventory/products.json', 'r') as f:
        product_list = json.load(f)

    products = []

    for item in product_list:
        products.append(Product(
            name = item['name'],
            description = item['description'],
            sku = item['sku'],
            category = ProductCategory.objects.get(name=item['category']),
            current_avg_cost = item['cost_price'],
            selling_price = item['selling_price'],
            current_stock = item['stock_quantity'],
            unit = item['unit'],
            reorder_level = item['reorder_level'],
            business=business,
            created_by=user
            )
        )

    Product.objects.bulk_create(products)