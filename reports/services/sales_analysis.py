from django.db.models import Sum, Count, Avg
from django.db.models.functions import TruncMonth
import logging

from sales.models import Sale

logger = logging.getLogger(__name__)

# Core function
def get_insights(business_id, from_date=None, to_date=None, customer_id=None, p_method=None):
    sales = get_filtered_query(business_id, from_date, to_date, customer_id, p_method)

    top_customers = get_top_customers(sales)
    payment_methods = get_payment_methods(sales)
    summary = get_summary(sales)
    sales_trend = get_sales_trend(sales)

    return {
        'top_customers': top_customers,
        'payment_methods': payment_methods,
        'summary': summary,
        'sales_trend': sales_trend
    }

def get_filtered_query(business_id, from_date, to_date, customer_id, p_method):
    sales = Sale.objects.filter(business_id=business_id, status=Sale.StatusChoices.COMPLETED).order_by('-sale_date')

    if from_date:
        sales = sales.filter(sale_date__gte=from_date)

    if to_date:
        sales = sales.filter(sale_date__lte=to_date)

    if customer_id:
        sales = sales.filter(customer_id=customer_id)

    if p_method:
        sales = sales.filter(payment_method=p_method)

    return sales


def get_top_customers(sales):
    return sales.values('customer', 'customer__name').annotate(
            revenue = Sum('total_amount'),
            orders = Count('id')
        ).order_by('-revenue')[:8]


def get_payment_methods(sales):
    payments_distribution = sales.values('payment_method').annotate(
        count = Count('id')
    ).order_by('-count')

    p_method_choices = dict(Sale.PaymentMethod.choices)

    payment_methods = {
        'labels': [],
        'count': []
    }

    for data in payments_distribution:
        payment_methods['labels'].append(p_method_choices.get(data['payment_method']))
        payment_methods['count'].append(data['count'])
    
    return payment_methods


def get_summary(sales):
    return sales.aggregate(
            total_revenue = Sum('total_amount'),
            total_sales_count = Count('id'),
            total_profit = Sum('total_profit'),
            avg_order_value = Avg('total_amount')
        )


def get_sales_trend(sales):
    monthly_sales = sales.annotate(
        month=TruncMonth('sale_date')
        ).values('month').annotate(
            total_amount=Sum('total_amount')
            ).order_by('month')
    
    sales_trend = {
        'labels': [],
        'data': []
    }

    for item in monthly_sales:
        sales_trend['labels'].append(item['month'].strftime('%b %Y'))
        sales_trend['data'].append(float(item['total_amount']))

    return sales_trend