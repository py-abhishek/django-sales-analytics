
from sales.models import Customer
import json


def seed_customers(business):

    with open('core/fixtures/customers.json', 'r') as f:
        customer_list = json.load(f)

    for c in customer_list:
        customer = Customer(
            name= c['name'],
            email=c['email'],
            phone=c['phone'],
            address=c['address'],
            business=business
        )
        customer.save()



        