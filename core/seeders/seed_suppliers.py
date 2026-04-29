
from purchases.models import Supplier
import json


def seed_suppliers(business):

    with open('core/fixtures/suppliers.json', 'r') as f:
        supplier_list = json.load(f)

    for s in supplier_list:
        supplier = Supplier(
            name= s['name'],
            email=s['email'],
            phone=s['phone'],
            address=s['address'],
            business=business
        )
        supplier.save()



        