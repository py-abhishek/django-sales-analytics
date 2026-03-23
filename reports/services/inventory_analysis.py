from django.db.models import Sum, Count
from django.db.models import Q, F

from inventory.models import Product, ProductCategory

def get_insights():
    products = get_filtered_query()
    summary = get_summary(products)
    inv_category_value = get_inv_category_value(products)
    distributed_stock = get_dist_stock(products)
    top_inventory_products = get_top_inv_products(products)
    low_stock_products = get_low_stock_products(products)
    out_of_stock_products = get_out_of_stock_products(products)

    return {
        'summary': summary,
        'inv_category_value': inv_category_value,
        'distributed_stock': distributed_stock,
        'top_inventory_products': top_inventory_products,
        'low_stock_products': low_stock_products,
        'out_of_stock_products': out_of_stock_products
    }


def get_filtered_query():
    products = Product.objects.all().order_by('-name')

    return products

def get_summary(products):
    result = products.aggregate(
        total_products = Count('id'),
        inventory_value = Sum(F('cost_price')* F('stock_quantity')),
        low_stock_count = Count('id', filter=Q(stock_quantity__lt=F('reorder_level'), stock_quantity__gt=0)),
        out_of_stock_count = Count('id', filter=Q(stock_quantity__exact=0)),
        in_stock_count=Sum('id', filter=Q(stock_quantity__gt=F('reorder_level')))
    )

    result['inventory_value'] = float(result['inventory_value'])

    return result

def get_inv_category_value(products):

    values = list(products.values(
        'category__name'
    ).annotate(
        total_value=Sum(F('cost_price') * F('stock_quantity'))
    ).order_by('-total_value')
    )

    result = {
        'labels': [v['category__name'] for v in values],
        'data': [float(v['total_value']) for v in values]
    }

    return result


def get_dist_stock(products):

    summary = get_summary(products)

    result = {
        'labels': ['In Stock', 'Low Stock', 'Out of Stock'],
        'data': [summary['in_stock_count'], summary['low_stock_count'], summary['out_of_stock_count']]
    }

    return result

def get_top_inv_products(products):
    top_products = list(products.values(
        'name'
    ).annotate(
        total_value=F('cost_price') * F('stock_quantity')
    ).order_by('-total_value')[:5]
    )

    result = {
        'labels': [tp['name'] for tp in top_products],
        'data': [float(tp['total_value']) for tp in top_products]
    }

    return result

def get_low_stock_products(products):
    return list(products.filter(
         Q(stock_quantity__lte=F('reorder_level'), stock_quantity__gt=0)
    ).order_by('stock_quantity').values(
        'id',
        'name',
        'reorder_level',
        'stock_quantity'
    )
    )

def get_out_of_stock_products(products):
    return list(products.filter(
         stock_quantity__exact=0
    ).order_by('stock_quantity').values(
        'id',
        'name',
        'reorder_level',
        'stock_quantity'
    )
    )