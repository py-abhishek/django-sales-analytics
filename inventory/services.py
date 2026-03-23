from django.db.models import Sum

def get_sales_insights(all_sales):
    totals =all_sales.aggregate(
        total_quantity_sold = Sum('quantity'),
        total_revenue = Sum('item_total_price'),
        total_profit = Sum('item_profit')
    )
    return { k: v or 0 for k, v in totals.items() }