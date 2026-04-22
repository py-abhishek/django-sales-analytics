from django.db.models import Sum, Count

from finance.models import Expense
from sales.models import Sale, SaleItem
from inventory.models import Product
from reports.services.revenue_exp_analysis import get_revenue_expense_trend, get_expense_by_category, get_profit_trend
from reports.services.product_analysis import get_low_stock_products, get_top_selling_products


def get_insights(business_id):

    sales, expenses, products, sale_items = get_filtered_queries(business_id)

    return {
        'summary': get_summary(sales, expenses),
        'rev_exp_trend': get_revenue_expense_trend(sales, expenses),
        'low_stock_products': get_low_stock_products(products),
        'top_selling_products': get_top_selling_products(sale_items),
        'exp_breakdown': get_expense_by_category(expenses),
        'profit_trend': get_profit_trend(sales, expenses)
    }
    


# Apply filters to each query
def get_filtered_queries(business_id):
    sales = Sale.objects.filter(business_id=business_id, status=Sale.StatusChoices.COMPLETED)
    expenses = Expense.objects.filter(business_id=business_id)
    products = Product.objects.filter(business_id=business_id)
    sale_items = SaleItem.objects.filter(business_id=business_id, sale__status=Sale.StatusChoices.COMPLETED)

    return sales, expenses, products, sale_items


def get_summary(sales, expenses):
    sales_data = sales.aggregate(
        total_revenue=Sum('total_amount'),
        total_sales=Count('id'),
        gross_profit=Sum('total_profit')
    )

    expense_data = expenses.aggregate(
        total_exps=Sum('amount')
    )

    net_profit = (sales_data['gross_profit'] or 0) - (expense_data['total_exps'] or 0)

    return {
        'total_revenue': sales_data['total_revenue'],
        'total_sales': sales_data['total_sales'],
        'total_exps': expense_data['total_exps'],
        'net_profit': net_profit
    }
