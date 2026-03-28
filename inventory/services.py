from django.db.models import Sum

from .models import InventoryLedger

def get_sales_insights(all_sales):
    totals =all_sales.aggregate(
        total_quantity_sold = Sum('quantity'),
        total_revenue = Sum('item_total_price'),
        total_profit = Sum('item_profit')
    )
    return { k: v or 0 for k, v in totals.items() }


def create_purchase_ledger(product, quantity, unit_cost, total_cost, purchase):
    InventoryLedger.objects.create(
        product = product,
        transaction_type = InventoryLedger.TransTypeChoices.PURCHASE,
        quantity_change = quantity,
        before_quantity = product.stock_quantity,
        after_quantity = product.stock_quantity + quantity,
        unit_cost = unit_cost,
        total_cost = total_cost,
        purchase = purchase
    )

def create_sale_ledger(product, quantity, unit_cost, total_cost, sale):
    InventoryLedger.objects.create(
        product = product,
        transaction_type = InventoryLedger.TransTypeChoices.SALE,
        quantity_change = (-quantity),
        before_quantity = product.stock_quantity,
        after_quantity = product.stock_quantity - quantity,
        unit_cost = unit_cost,
        total_cost = total_cost,
        sale = sale
    )
    
    