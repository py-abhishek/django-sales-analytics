from django.db.models import Sum, Count, Avg
from django.db.models.functions import TruncMonth
import logging

logger = logging.getLogger(__name__)

def get_insights(sales):
    # Getting top customers
    top_customers = sales.values('customer', 'customer__name').annotate(
        revenue = Sum('total_amount'),
        orders = Count('id')
    ).order_by('-revenue')[:8]

    # Getting payment methods distribution
    payments_distribution = sales.values('payment_method').annotate(
        count = Count('id')
    ).order_by('-count')

    payment_methods = {
        'labels': [],
        'count': []
    }

    for data in payments_distribution:
        payment_methods['labels'].append(data['payment_method'].upper())
        payment_methods['count'].append(data['count'])


    # Totals
    sales_insights = sales.aggregate(
        total_revenue = Sum('total_amount'),
        total_sales_count = Count('id'),
        total_profit = Sum('total_profit'),
        avg_order_value = Avg('total_amount')
    )
    # logger.info(sales_insights)

    # Getting monthly sales data
    monthly_sales = sales.annotate(month=TruncMonth('sale_date')).values('month').annotate(total_amount=Sum('total_amount')).order_by('month')
    sales_trend = {
        'labels': [],
        'data': []
    }

    for data in monthly_sales:
        sales_trend['labels'].append(data['month'].strftime('%b %Y'))
        sales_trend['data'].append(float(data['total_amount']))


    return {
        'top_customers': top_customers,
        'payment_methods': payment_methods,
        'sales_insights': sales_insights,
        'sales_trend': sales_trend
    }
