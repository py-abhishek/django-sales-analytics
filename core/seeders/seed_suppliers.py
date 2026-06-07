
from purchases.models import Supplier
import json


def seed_suppliers(data, business):

    with open(data, 'r') as f:
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



        