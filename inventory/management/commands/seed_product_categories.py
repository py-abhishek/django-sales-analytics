from django.core.management.base import BaseCommand

from inventory.models import ProductCategory


class Command(BaseCommand):
    help = 'Create sample products categories'

    categories = [

        {'name': 'Laptops', 'description': 'Personal and business laptops including ultrabooks and gaming laptops'},

        {'name': 'Desktop Computers', 'description': 'Complete desktop systems and computer workstations'},

        {'name': 'Computer Accessories', 'description': 'Keyboards, mice, mousepads, and other computer peripherals'},

        {'name': 'Monitors & Displays', 'description': 'LED, LCD, and gaming monitors used for computers and workstations'},

        {'name': 'Storage Devices', 'description': 'Hard drives, SSDs, USB drives, and other digital storage devices'},

        {'name': 'Networking Equipment', 'description': 'Routers, modems, switches, and networking accessories'},

        {'name': 'Printers & Scanners', 'description': 'Inkjet printers, laser printers, scanners, and multifunction devices'},

        {'name': 'Audio Devices', 'description': 'Headphones, earphones, speakers, and sound systems'},

        {'name': 'Mobile Accessories', 'description': 'Chargers, cables, power banks, phone cases, and screen protectors'},

        {'name': 'Smart Devices', 'description': 'Smart watches, fitness bands, and other connected smart gadgets'},

        {'name': 'Cables & Adapters', 'description': 'HDMI cables, USB cables, converters, and various electronic adapters'},

        {'name': 'Power Solutions', 'description': 'UPS systems, extension boards, surge protectors, and power supplies'}

    ]    

    def handle(self, *args, **options):

        product_categories = []
        for item in self.categories:
            product_categories.append(ProductCategory(**item))

        ProductCategory.objects.bulk_create(product_categories)
        print("Data Inserted Successfully")
        

        