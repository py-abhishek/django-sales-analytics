from django.core.management.base import BaseCommand
from inventory.models import Product, ProductCategory


class Command(BaseCommand):
    help = 'Create sample products'

    product_list = [

        {
        'name': 'Dell Inspiron 15 Laptop',
        'description': '15.6 inch business laptop with Intel i5 processor and 8GB RAM',
        'sku': 'LAP-DEL-1001',
        'category': 'Laptops',
        'cost_price': 42000,
        'selling_price': 48500,
        'stock_quantity': 520,
        'unit': Product.UnitChoices.PIECE,
        'reorder_level': 104
        },

        {
        'name': 'HP Pavilion 24 LED Monitor',
        'description': '24 inch full HD IPS monitor for office and gaming',
        'sku': 'MON-HP-2001',
        'category': 'Monitors & Displays',
        'cost_price': 7800,
        'selling_price': 9400,
        'stock_quantity': 850,
        'unit': Product.UnitChoices.PIECE,
        'reorder_level': 170
        },

        {
        'name': 'Logitech Wireless Mouse M235',
        'description': 'Compact wireless optical mouse with nano receiver',
        'sku': 'ACC-LOG-3001',
        'category': 'Computer Accessories',
        'cost_price': 420,
        'selling_price': 650,
        'stock_quantity': 4800,
        'unit': Product.UnitChoices.PIECE,
        'reorder_level': 720
        },

        {
        'name': 'Dell Multimedia Keyboard KB216',
        'description': 'Full-size USB keyboard with chiclet keys',
        'sku': 'ACC-DEL-3002',
        'category': 'Computer Accessories',
        'cost_price': 520,
        'selling_price': 780,
        'stock_quantity': 3500,
        'unit': Product.UnitChoices.PIECE,
        'reorder_level': 700
        },

        {
        'name': 'Samsung 1TB Portable SSD',
        'description': 'High speed external SSD with USB 3.2 support',
        'sku': 'STO-SAM-4001',
        'category': 'Storage Devices',
        'cost_price': 6200,
        'selling_price': 7500,
        'stock_quantity': 900,
        'unit': Product.UnitChoices.PIECE,
        'reorder_level': 180
        },

        {
        'name': 'Seagate 2TB External Hard Drive',
        'description': 'Portable HDD for backup and storage',
        'sku': 'STO-SEA-4002',
        'category': 'Storage Devices',
        'cost_price': 5200,
        'selling_price': 6500,
        'stock_quantity': 1200,
        'unit': Product.UnitChoices.PIECE,
        'reorder_level': 240
        },

        {
        'name': 'TP-Link Dual Band WiFi Router',
        'description': 'AC1200 high speed wireless router',
        'sku': 'NET-TPL-5001',
        'category': 'Networking Equipment',
        'cost_price': 1800,
        'selling_price': 2400,
        'stock_quantity': 2000,
        'unit': Product.UnitChoices.PIECE,
        'reorder_level': 300
        },

        {
        'name': 'D-Link 8 Port Gigabit Switch',
        'description': 'Unmanaged ethernet switch for office networking',
        'sku': 'NET-DLK-5002',
        'category': 'Networking Equipment',
        'cost_price': 2100,
        'selling_price': 2800,
        'stock_quantity': 1100,
        'unit': Product.UnitChoices.PIECE,
        'reorder_level': 220
        },

        {
        'name': 'Boat Rockerz 450 Bluetooth Headphones',
        'description': 'Wireless over ear headphones with deep bass',
        'sku': 'AUD-BOA-6001',
        'category': 'Audio Devices',
        'cost_price': 980,
        'selling_price': 1499,
        'stock_quantity': 5400,
        'unit': Product.UnitChoices.PIECE,
        'reorder_level': 1080
        },

        {
        'name': 'JBL Go 3 Portable Bluetooth Speaker',
        'description': 'Compact waterproof portable speaker',
        'sku': 'AUD-JBL-6002',
        'category': 'Audio Devices',
        'cost_price': 1800,
        'selling_price': 2499,
        'stock_quantity': 2600,
        'unit': Product.UnitChoices.PIECE,
        'reorder_level': 520
        },

        {
        'name': 'Mi 20000mAh Power Bank',
        'description': 'Fast charging portable power bank',
        'sku': 'MOB-MI-7001',
        'category': 'Mobile Accessories',
        'cost_price': 980,
        'selling_price': 1399,
        'stock_quantity': 4100,
        'unit': Product.UnitChoices.PIECE,
        'reorder_level': 820
        },

        {
        'name': 'Anker USB-C Fast Charging Cable',
        'description': 'Durable USB C charging cable for smartphones',
        'sku': 'CAB-ANK-8001',
        'category': 'Cables & Adapters',
        'cost_price': 120,
        'selling_price': 299,
        'stock_quantity': 7200,
        'unit': Product.UnitChoices.PIECE,
        'reorder_level': 1440
        },

        {
        'name': 'Belkin HDMI 2.0 Cable 2 Meter',
        'description': 'High speed HDMI cable supporting 4K video',
        'sku': 'CAB-BEL-8002',
        'category': 'Cables & Adapters',
        'cost_price': 220,
        'selling_price': 450,
        'stock_quantity': 3800,
        'unit': 'm',
        'reorder_level': 760
        },

        {
        'name': 'APC 650VA UPS Backup',
        'description': 'Power backup UPS for desktop computers',
        'sku': 'POW-APC-9001',
        'category': 'Power Solutions',
        'cost_price': 3200,
        'selling_price': 4200,
        'stock_quantity': 700,
        'unit': Product.UnitChoices.PIECE,
        'reorder_level': 140
        },

        {
        'name': 'Syska 6 Socket Extension Board',
        'description': 'Surge protected power extension board',
        'sku': 'POW-SYS-9002',
        'category': 'Power Solutions',
        'cost_price': 450,
        'selling_price': 750,
        'stock_quantity': 3200,
        'unit': Product.UnitChoices.PIECE,
        'reorder_level': 640
        }

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

        