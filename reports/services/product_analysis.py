from django.db.models import Sum, Count, Q, F, Max
from django.db.models.functions import TruncMonth
from sales.models import SaleItem
from inventory.models import Product

# Core function
def get_insights(from_date=None, to_date=None, category=None):

    sale_items, products = get_filtered_query(from_date, to_date, category)
    
    summary = get_summary(products, sale_items)
    product_sales_trend = get_product_sales_trend(sale_items)
    top_selling_products = get_top_selling_products(sale_items)
    top_categories = get_top_categories(sale_items)
    slow_products = get_slow_moving_products(sale_items)
    low_stock_products = get_low_stock_products(products)

    return {
        'summary': summary,
        'product_sales_trend': product_sales_trend,
        'top_selling_products': top_selling_products,
        'top_categories': top_categories,
        'slow_products': slow_products,
        'low_stock_products': low_stock_products
    }

def get_filtered_query(from_date=None, to_date=None, category=None):
    sale_items = SaleItem.objects.select_related('product', 'sale')
    products = Product.objects.all()

    if from_date:
        sale_items = sale_items.filter(sale__sale_date__gte=from_date)

    if to_date:
        sale_items = sale_items.filter(sale__sale_date__lte=to_date)

    if category:
        sale_items = sale_items.filter(product__category_id=category)
        products = products.filter(category_id=category)

    return sale_items, products


def get_summary(products, sale_items):
    sale_items_summary = sale_items.aggregate(
        units_sold = Sum('quantity'),
        product_revenue = Sum(F('price_at_sale') * F('quantity'))
    )
    summary = {
        'units_sold': sale_items_summary['units_sold'],
        'product_revenue': float(sale_items_summary['product_revenue'] or 0),
    }

    summary.update(products.aggregate(
        total_products = Count('id'),
        low_stock_products = Count('id', filter=Q(current_stock__lt=F('reorder_level'))),
    ))
    
    return summary


def get_product_sales_trend(sale_items):
    monthly_units_sold = sale_items.annotate(
        month=TruncMonth('sale__sale_date')
        ).values('month').annotate(
            total_units=Sum('quantity')
            ).order_by('month')

    product_sales_trend = {
        'labels': [],
        'data': []
    }

    for item in monthly_units_sold:
        month = item['month']
        product_sales_trend['labels'].append(month.strftime('%b %Y') if month else '')
        product_sales_trend['data'].append(item['total_units'])

    return product_sales_trend


def get_top_selling_products(sale_items):
    top_selling_products = sale_items.values(
        'product__sku', 'product__name'
    ).annotate(
        total_units_sold = Sum('quantity')
        ).order_by('-total_units_sold')[:5]
    
    top_products = {
        'labels': [],
        'data': []
    }

    for item in top_selling_products:
        top_products['labels'].append(item['product__name'])
        top_products['data'].append(item['total_units_sold'])

    return top_products


def get_top_categories(sale_items):
    categories = list(
        sale_items.values(
        'product__category__name'
        ).annotate(
            total_units_sold = Sum('quantity')
        ).order_by('-total_units_sold')
    )
    
    top_categories = {
        'labels': [],
        'data': []
    }

    for item in categories[:5]:
        top_categories['labels'].append(item['product__category__name'])
        top_categories['data'].append(item['total_units_sold'])

    others = sum(item['total_units_sold'] for item in categories[5:])
    
    if others > 0:
        top_categories['labels'].append('others')
        top_categories['data'].append(others)

    return top_categories


def get_slow_moving_products(sale_items):
    slow_products = sale_items.values(
        'product__sku', 'product__name'
    ).annotate(
        total_units_sold = Sum('quantity'),
        last_sale_date = Max('sale__sale_date')
        ).order_by('total_units_sold')[:5]
    
    result = []

    for product in slow_products:
        result.append({
            'product_name': product['product__name'],
            'total_units_sold': product['total_units_sold'],
            'last_sale_date': product['last_sale_date'].isoformat(),
        })

    return result


def get_low_stock_products(products):
    return list(products.filter(
        current_stock__lt=F('reorder_level')
    ).order_by('current_stock')[:5].values(
        'id',
        'name',
        'current_stock',
        'reorder_level'
    ))