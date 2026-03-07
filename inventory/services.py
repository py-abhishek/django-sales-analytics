from django.db.models import Sum

def get_sales_insights(all_sales):
    sales_insights = {
        'total_quantity_sold': total_sold(all_sales),
        'total_revenue': total_revenue(all_sales),
        'total_profit': total_profit(all_sales)
    }
    return sales_insights


def total_sold(all_sales):
    return all_sales.aggregate(
        total = Sum("quantity")
    )["total"] or 0


def total_revenue(all_sales):
    return all_sales.aggregate(
        total = Sum("item_total")
    )["total"] or 0


def total_profit(all_sales):
    return all_sales.aggregate(
        total = Sum("item_profit")
    )["total"] or 0