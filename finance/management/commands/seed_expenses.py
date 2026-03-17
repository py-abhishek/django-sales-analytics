from django.core.management.base import BaseCommand
from finance.models import Expense, ExpenseCategory


class Command(BaseCommand):
    help = 'Create sample expense'

    expense_list = [

        {
        'name': 'Office Rent January',
        'category': 'Office Rent',
        'amount': 45000,
        'description': 'Monthly office rent payment',
        'expense_date': '2025-03-20'
        },

        {
        'name': 'Office Rent February',
        'category': 'Office Rent',
        'amount': 45000,
        'description': 'Monthly office rent payment',
        'expense_date': '2025-04-20'
        },

        {
        'name': 'Office Rent March',
        'category': 'Office Rent',
        'amount': 45000,
        'description': 'Monthly office rent payment',
        'expense_date': '2025-05-20'
        },

        {
        'name': 'Office Electricity Bill',
        'category': 'Electricity Bills',
        'amount': 10900,
        'description': 'Monthly electricity usage charges',
        'expense_date': '2025-04-05'
        },

        {
        'name': 'Office Electricity Bill',
        'category': 'Electricity Bills',
        'amount': 5900,
        'description': 'Monthly electricity usage charges',
        'expense_date': '2025-05-05'
        },

        {
        'name': 'Office Electricity Bill',
        'category': 'Electricity Bills',
        'amount': 6400,
        'description': 'Monthly electricity usage charges',
        'expense_date': '2025-06-05'
        },

        {
        'name': 'Broadband Internet Bill',
        'category': 'Internet and WiFi',
        'amount': 1800,
        'description': 'Monthly fiber broadband plan',
        'expense_date': '2025-04-10'
        },

        {
        'name': 'Broadband Internet Bill',
        'category': 'Internet and WiFi',
        'amount': 1800,
        'description': 'Monthly fiber broadband plan',
        'expense_date': '2025-05-10'
        },

        {
        'name': 'Broadband Internet Bill',
        'category': 'Internet and WiFi',
        'amount': 1800,
        'description': 'Monthly fiber broadband plan',
        'expense_date': '2025-06-10'
        },

        {
        'name': 'Employee Salary Payment',
        'category': 'Employee Salaries',
        'amount': 120000,
        'description': 'Monthly salary disbursement for staff',
        'expense_date': '2025-04-01'
        },

        {
        'name': 'Employee Salary Payment',
        'category': 'Employee Salaries',
        'amount': 120000,
        'description': 'Monthly salary disbursement for staff',
        'expense_date': '2025-05-01'
        },

        {
        'name': 'Employee Salary Payment',
        'category': 'Employee Salaries',
        'amount': 120000,
        'description': 'Monthly salary disbursement for staff',
        'expense_date': '2025-06-01'
        },

        {
        'name': 'Freelance Graphic Design',
        'category': 'Freelancer Payments',
        'amount': 8000,
        'description': 'Payment for marketing creatives',
        'expense_date': '2025-04-15'
        },

        {
        'name': 'Freelance Content Writing',
        'category': 'Freelancer Payments',
        'amount': 6500,
        'description': 'Blog and marketing content writing',
        'expense_date': '2025-05-18'
        },

        {
        'name': 'Freelance Web Development',
        'category': 'Freelancer Payments',
        'amount': 15000,
        'description': 'Landing page development work',
        'expense_date': '2025-06-21'
        },

        {
        'name': 'Stationery Purchase',
        'category': 'Office Supplies',
        'amount': 1200,
        'description': 'Pens, paper and markers',
        'expense_date': '2025-04-08'
        },

        {
        'name': 'Printer Paper Bulk',
        'category': 'Office Supplies',
        'amount': 2200,
        'description': 'Bulk purchase of A4 paper',
        'expense_date': '2025-05-12'
        },

        {
        'name': 'Office Files and Folders',
        'category': 'Office Supplies',
        'amount': 900,
        'description': 'Office document folders',
        'expense_date': '2025-06-13'
        },

        {
        'name': 'Project Management Software',
        'category': 'Software Subscriptions',
        'amount': 2500,
        'description': 'Monthly SaaS project tool subscription',
        'expense_date': '2025-04-03'
        },

        {
        'name': 'Email Marketing Tool',
        'category': 'Software Subscriptions',
        'amount': 1800,
        'description': 'Email automation subscription',
        'expense_date': '2025-05-03'
        },

        {
        'name': 'Design Software Subscription',
        'category': 'Software Subscriptions',
        'amount': 3200,
        'description': 'Graphic design SaaS tools',
        'expense_date': '2025-06-03'
        },

        {
        'name': 'Google Ads Campaign',
        'category': 'Marketing and Advertising',
        'amount': 15000,
        'description': 'Search advertising campaign',
        'expense_date': '2025-05-11'
        },

        {
        'name': 'Local Newspaper Ad',
        'category': 'Marketing and Advertising',
        'amount': 8000,
        'description': 'Local newspaper business promotion',
        'expense_date': '2025-06-16'
        },

        {
        'name': 'Brand Promotion Campaign',
        'category': 'Marketing and Advertising',
        'amount': 12000,
        'description': 'Online marketing promotion',
        'expense_date': '2025-07-02'
        },

        {
        'name': 'Employee Salary Payment',
        'category': 'Employee Salaries',
        'amount': 150000,
        'description': 'Monthly salary disbursement for staff',
        'expense_date': '2025-07-01'
        },

        {
        'name': 'Instagram Promotion',
        'category': 'Social Media Marketing',
        'amount': 5000,
        'description': 'Promoted product campaign',
        'expense_date': '2025-05-20'
        },

        {
        'name': 'Facebook Ads Campaign',
        'category': 'Social Media Marketing',
        'amount': 6500,
        'description': 'Lead generation campaign',
        'expense_date': '2025-06-20'
        },

        {
        'name': 'LinkedIn Sponsored Post',
        'category': 'Social Media Marketing',
        'amount': 7200,
        'description': 'Professional audience targeting',
        'expense_date': '2025-07-12'
        },

        {
        'name': 'Business Trip Train Ticket',
        'category': 'Travel Expenses',
        'amount': 3500,
        'description': 'Client meeting travel expense',
        'expense_date': '2025-05-25'
        },

        {
        'name': 'Hotel Stay for Conference',
        'category': 'Travel Expenses',
        'amount': 8200,
        'description': 'Business conference accommodation',
        'expense_date': '2025-07-18'
        },

        {
        'name': 'Taxi Fare for Client Meeting',
        'category': 'Travel Expenses',
        'amount': 1200,
        'description': 'Local travel for meeting',
        'expense_date': '2025-06-15'
        },

        {
        'name': 'Vehicle Fuel Refill',
        'category': 'Fuel Costs',
        'amount': 3000,
        'description': 'Fuel for office vehicle',
        'expense_date': '2025-05-02'
        },

        {
        'name': 'Vehicle Fuel Refill',
        'category': 'Fuel Costs',
        'amount': 2800,
        'description': 'Fuel for office vehicle',
        'expense_date': '2025-06-02'
        },

        {
        'name': 'Vehicle Fuel Refill',
        'category': 'Fuel Costs',
        'amount': 3100,
        'description': 'Fuel for office vehicle',
        'expense_date': '2025-07-02'
        },

        {
        'name': 'New Office Laptop',
        'category': 'Equipment Purchase',
        'amount': 62000,
        'description': 'Laptop for development team',
        'expense_date': '2025-06-14'
        },

        {
        'name': 'Employee Salary Payment',
        'category': 'Employee Salaries',
        'amount': 145000,
        'description': 'Monthly salary disbursement for staff',
        'expense_date': '2025-05-01'
        },

        {
        'name': 'Office Printer Purchase',
        'category': 'Equipment Purchase',
        'amount': 18500,
        'description': 'High speed office printer',
        'expense_date': '2025-07-07'
        },

        {
        'name': 'Desk Computer Purchase',
        'category': 'Equipment Purchase',
        'amount': 42000,
        'description': 'Desktop system for operations',
        'expense_date': '2025-08-05'
        },

        {
        'name': 'Printer Repair',
        'category': 'Equipment Maintenance',
        'amount': 1500,
        'description': 'Printer service and repair',
        'expense_date': '2025-06-19'
        },

        {
        'name': 'Computer Service',
        'category': 'Equipment Maintenance',
        'amount': 2500,
        'description': 'Annual computer servicing',
        'expense_date': '2025-08-10'
        },

        {
        'name': 'Employee Salary Payment',
        'category': 'Employee Salaries',
        'amount': 120000,
        'description': 'Monthly salary disbursement for staff',
        'expense_date': '2025-09-01'
        },

        {
        'name': 'Website Hosting Renewal',
        'category': 'Hosting and Domain',
        'amount': 3200,
        'description': 'Annual web hosting plan',
        'expense_date': '2025-07-25'
        },

        {
        'name': 'Domain Renewal',
        'category': 'Hosting and Domain',
        'amount': 900,
        'description': 'Domain name renewal',
        'expense_date': '2025-08-25'
        },

        {
        'name': 'Employee Training Workshop',
        'category': 'Training and Development',
        'amount': 120000,
        'description': 'Skill improvement workshop',
        'expense_date': '2025-09-02'
        },

        {
        'name': 'Online Course Subscription',
        'category': 'Training and Development',
        'amount': 3500,
        'description': 'Professional development course',
        'expense_date': '2025-09-15'
        },

        {
        'name': 'Legal Consultation',
        'category': 'Legal and Compliance',
        'amount': 10000,
        'description': 'Contract review and legal advice',
        'expense_date': '2025-08-17'
        },

        {
        'name': 'Company Registration Renewal',
        'category': 'Legal and Compliance',
        'amount': 6000,
        'description': 'Annual compliance filing',
        'expense_date': '2025-09-20'
        },

        {
        'name': 'Accounting Service Fee',
        'category': 'Accounting Services',
        'amount': 7000,
        'description': 'Monthly accounting service',
        'expense_date': '2025-07-05'
        },

        {
        'name': 'Accounting Service Fee',
        'category': 'Accounting Services',
        'amount': 7000,
        'description': 'Monthly accounting service',
        'expense_date': '2025-08-05'
        },

        {
        'name': 'Bank Transaction Charges',
        'category': 'Bank Charges',
        'amount': 450,
        'description': 'Monthly bank transaction fees',
        'expense_date': '2025-07-30'
        },

        {
        'name': 'Payment Gateway Charges',
        'category': 'Bank Charges',
        'amount': 1200,
        'description': 'Online payment processing charges',
        'expense_date': '2025-08-30'
        },

        {
        'name': 'Packaging Boxes',
        'category': 'Packaging Materials',
        'amount': 5200,
        'description': 'Bulk purchase of packaging boxes',
        'expense_date': '2025-09-01'
        },

        {
        'name': 'Packing Tape and Labels',
        'category': 'Packaging Materials',
        'amount': 1100,
        'description': 'Shipping label materials',
        'expense_date': '2025-09-03'
        },

        {
        'name': 'Employee Salary Payment',
        'category': 'Employee Salaries',
        'amount': 120000,
        'description': 'Monthly salary disbursement for staff',
        'expense_date': '2025-10-01'
        },

        {
        'name': 'Courier Delivery Charges',
        'category': 'Shipping and Delivery',
        'amount': 6200,
        'description': 'Courier partner delivery fees',
        'expense_date': '2025-09-07'
        },

        {
        'name': 'Logistics Shipment Cost',
        'category': 'Shipping and Delivery',
        'amount': 8500,
        'description': 'Bulk shipment delivery',
        'expense_date': '2025-09-21'
        },

        {
        'name': 'Office Cleaning Service',
        'category': 'Office Cleaning',
        'amount': 2500,
        'description': 'Monthly office cleaning service',
        'expense_date': '2025-10-02'
        },

        {
        'name': 'Deep Cleaning Service',
        'category': 'Office Cleaning',
        'amount': 4800,
        'description': 'Quarterly office cleaning',
        'expense_date': '2025-12-01'
        },

        {
        'name': 'Office Chairs Purchase',
        'category': 'Furniture and Fixtures',
        'amount': 14000,
        'description': 'Purchase of ergonomic office chairs',
        'expense_date': '2025-10-18'
        },

        {
        'name': 'Reception Desk Purchase',
        'category': 'Furniture and Fixtures',
        'amount': 20000,
        'description': 'New reception desk furniture',
        'expense_date': '2025-11-11'
        },

        {
        'name': 'Employee Salary Payment',
        'category': 'Employee Salaries',
        'amount': 160000,
        'description': 'Monthly salary disbursement for staff',
        'expense_date': '2025-11-01'
        },

        {
        'name': 'Water Supply Bill',
        'category': 'Utilities',
        'amount': 900,
        'description': 'Monthly water supply bill',
        'expense_date': '2025-10-05'
        },

        {
        'name': 'Water Supply Bill',
        'category': 'Utilities',
        'amount': 950,
        'description': 'Monthly water supply bill',
        'expense_date': '2025-11-05'
        },

        {
        'name': 'Employee Salary Payment',
        'category': 'Employee Salaries',
        'amount': 140000,
        'description': 'Monthly salary disbursement for staff',
        'expense_date': '2025-12-01'
        },

        {
        'name': 'Water Supply Bill',
        'category': 'Utilities',
        'amount': 5000,
        'description': 'Monthly water supply bill',
        'expense_date': '2025-12-05'
        },

        {
        'name': 'Employee Salary Payment',
        'category': 'Employee Salaries',
        'amount': 130000,
        'description': 'Monthly salary disbursement for staff',
        'expense_date': '2026-01-01'
        },
        
        {
        'name': 'Employee Salary Payment',
        'category': 'Employee Salaries',
        'amount': 130000,
        'description': 'Monthly salary disbursement for staff',
        'expense_date': '2026-02-01'
        }

]


    expense = []

    def handle(self, *args, **options):

        for item in self.expense_list:
            expense = Expense(
                name=item['name'],
                category=ExpenseCategory.objects.get(name=item['category']),
                amount=item['amount'],
                description= item['description'],
                expense_date=item['expense_date']
            )
            
            self.expense.append(expense)

        Expense.objects.bulk_create(self.expense)
        print("Expenses added successfully")

        