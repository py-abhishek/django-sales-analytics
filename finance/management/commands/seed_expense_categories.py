from django.core.management.base import BaseCommand

from finance.models import ExpenseCategory


class Command(BaseCommand):
    help = 'Create sample expense categories'

    categories = [
        {
            'name': 'Office Rent',
            'description': 'Monthly rent paid for office or workspace'
        },
        {
            'name': 'Electricity Bills',
            'description': 'Electricity charges for office operations'
        },
        {
            'name': 'Internet and WiFi',
            'description': 'Monthly internet and broadband expenses'
        },
        {
            'name': 'Employee Salaries',
            'description': 'Monthly salaries paid to employees'
        },
        {
            'name': 'Freelancer Payments',
            'description': 'Payments made to freelance workers or contractors'
        },
        {
            'name': 'Office Supplies',
            'description': 'Expenses for stationery, paper, pens, and office materials'
        },
        {
            'name': 'Software Subscriptions',
            'description': 'Payments for software tools and SaaS platforms'
        },
        {
            'name': 'Marketing and Advertising',
            'description': 'Expenses on digital ads, promotions, and campaigns'
        },
        {
            'name': 'Social Media Marketing',
            'description': 'Paid promotions and marketing activities on social platforms'
        },
        {
            'name': 'Travel Expenses',
            'description': 'Business travel expenses including transport and lodging'
        },
        {
            'name': 'Fuel Costs',
            'description': 'Fuel expenses for company vehicles or deliveries'
        },
        {
            'name': 'Equipment Purchase',
            'description': 'Expenses for buying office equipment and devices'
        },
        {
            'name': 'Equipment Maintenance',
            'description': 'Repair and maintenance of office equipment'
        },
        {
            'name': 'Hosting and Domain',
            'description': 'Website hosting and domain registration expenses'
        },
        {
            'name': 'Training and Development',
            'description': 'Employee training programs and professional development'
        },
        {
            'name': 'Legal and Compliance',
            'description': 'Legal consultation and compliance related costs'
        },
        {
            'name': 'Accounting Services',
            'description': 'Payments made to accountants or accounting services'
        },
        {
            'name': 'Bank Charges',
            'description': 'Bank fees, transaction charges, and service costs'
        },
        {
            'name': 'Packaging Materials',
            'description': 'Boxes, bags, and packaging supplies for products'
        },
        {
            'name': 'Shipping and Delivery',
            'description': 'Courier and logistics expenses for product delivery'
        },
        {
            'name': 'Office Cleaning',
            'description': 'Cleaning and housekeeping services for the office'
        },
        {
            'name': 'Furniture and Fixtures',
            'description': 'Purchase or repair of office furniture and fixtures'
        },
        {
            'name': 'Utilities',
            'description': 'Water bills and other utility expenses'
        }
    ]
 

    def handle(self, *args, **options):

        expense_categories = []
        for item in self.categories:
            expense_categories.append(ExpenseCategory(**item))

        ExpenseCategory.objects.bulk_create(expense_categories)
        print("Data Inserted Successfully")
        

        