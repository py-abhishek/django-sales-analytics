import json

from inventory.models import ProductCategory, Product
from inventory.services import new_product_ledger

def seed_products(business, user):
    with open('core/fixtures/inventory/products.json', 'r') as f:
        product_list = json.load(f)

    products = []

    for item in product_list:
        product = Product(
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
        
        # Save product
        product.save()
        
        # Create new product ledger
        new_product_ledger(
            product,
            item['stock_quantity'],
            item['cost_price'],
            item['cost_price']*item['stock_quantity'],
            business.id
        )
        