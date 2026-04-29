from django.db.models import Sum

from .models import InventoryLedger

# Core function
def get_sales_insights(all_sales, business_id):
    totals =all_sales.aggregate(
        total_quantity_sold = Sum('quantity'),
        total_revenue = Sum('item_total_price'),
        total_profit = Sum('item_profit')
    )
    return { k: v or 0 for k, v in totals.items() }

# Record purchase history
def create_purchase_ledger(product, quantity, unit_cost, total_cost, purchase, business_id):
    
    InventoryLedger.objects.create(
        product = product,
        transaction_type = InventoryLedger.TransTypeChoices.PURCHASE,
        quantity_change = quantity,
        before_quantity = product.current_stock,
        after_quantity = product.current_stock + quantity,
        unit_cost = unit_cost,
        total_cost = total_cost,
        purchase = purchase,
        business_id=business_id
    )

# Record sales history
def create_sale_ledger(product, quantity, unit_cost, total_cost, sale, business_id):
    InventoryLedger.objects.create(
        product = product,
        transaction_type = InventoryLedger.TransTypeChoices.SALE,
        quantity_change = (-quantity),
        before_quantity = product.current_stock,
        after_quantity = product.current_stock - quantity,
        unit_cost = unit_cost,
        total_cost = total_cost,
        sale = sale,
        business_id=business_id
    )

# New product history
def new_product_ledger(product, quantity, unit_cost, total_cost, business_id):
    if int(quantity) == 0:
        return
    
    InventoryLedger.objects.create(
        product = product,
        transaction_type = InventoryLedger.TransTypeChoices.NEW_PRODUCT,
        quantity_change = quantity,
        before_quantity = 0,
        after_quantity = quantity,
        unit_cost = unit_cost,
        total_cost = total_cost,
        business_id=business_id
    )
    

# Calculate new average cost
def calc_new_avg_cost(product, new_qty, new_cost):
    old_stock = product.current_stock
    old_avg_cost = product.current_avg_cost

    # calc new average cost
    new_avg_cost = ((old_stock * old_avg_cost) + (new_qty * new_cost)) / (old_stock + new_qty)
    return new_avg_cost

# Record cancel sale entry
def create_cancel_sale_ledger(business_id, sale, product, quantity, cost_at_sale):
    InventoryLedger.objects.create(
        product = product,
        transaction_type = InventoryLedger.TransTypeChoices.CANCEL_SALE,
        quantity_change = quantity,
        before_quantity = product.current_stock,
        after_quantity = product.current_stock + quantity,
        unit_cost = cost_at_sale,
        total_cost = cost_at_sale * quantity,
        sale=sale,
        business_id=business_id
    )