from sales.models import Sale
from finance.models import Expense
from django.db.models import Sum
from django.db.models.functions import TruncMonth

def get_insights():
    sales, expenses = get_filtered_queries()

    summary = get_summary(sales, expenses)
    revenue_expense_trend = get_revenue_expense_trend(sales, expenses)
    profit_trend = get_profit_trend(sales, expenses)
    exp_by_category = get_expense_by_category(expenses)

    return {
        'summary': summary,
        'revenue_expense_trend': revenue_expense_trend,
        'profit_trend': profit_trend,
        'exp_by_category': exp_by_category
    }


def get_filtered_queries():
    sales = Sale.objects.all()
    expenses = Expense.objects.all()

    return sales, expenses

def get_summary(sales, expenses):
    summary = sales.aggregate(
        total_revenue = Sum('total_amount'),
        total_profit = Sum('total_profit')
    )

    summary.update(
        expenses.aggregate(
            total_expense = Sum('amount')
        )
    )

    total_revenue = summary.get('total_revenue') or 0
    total_profit = summary.get('total_profit') or 0
    total_expense = summary.get('total_expense') or 0

    net_profit = total_profit - total_expense
    
    if  total_revenue > 0:
        profit_margin = round((net_profit / summary['total_revenue']) * 100, 2)
    else:
        profit_margin = 0

    summary['total_revenue'] = total_revenue
    summary['total_expense'] = total_expense
    summary['net_profit'] = net_profit
    summary['profit_margin'] = profit_margin

    return summary


def get_revenue_expense_trend(sales, expenses):
    # Revenue
    monthly_rev = sales.annotate(
        month=TruncMonth('sale_date')
        ).values('month').annotate(
            total_revenue=Sum('total_amount')
            ).order_by('month')
    
    # Expenses
    monthly_exp = expenses.annotate(
        month=TruncMonth('expense_date')
        ).values('month').annotate(
            total_expense=Sum('amount')
            ).order_by('month')
    
    revenue_dict = { r['month']: float(r['total_revenue']) for r in monthly_rev }
    expense_dict = { e['month']: float(e['total_expense']) for e in monthly_exp }

    all_months = sorted(set(revenue_dict) | set(expense_dict))
    
    result = {
        'labels': [],
        'revenue': [],
        'expense': []
    }

    for month in all_months:
        result['labels'].append(month.strftime('%b %Y'))
        result['revenue'].append(revenue_dict.get(month, 0))
        result['expense'].append(expense_dict.get(month, 0))


    return result


def get_profit_trend(sales, expenses):
    monthly_profit = sales.annotate(
        month=TruncMonth('sale_date')
        ).values('month').annotate(
            total_profit=Sum('total_profit')
        )
    
    monthly_exp = expenses.annotate(
        month=TruncMonth('expense_date')
        ).values('month').annotate(
            total_expense=Sum('amount')
        )
    
    profit_dict = { p['month']: float(p['total_profit']) for p in monthly_profit }
    exp_dict = { e['month']: float(e['total_expense']) for e in monthly_exp }

    all_months = sorted(set(profit_dict) | set(exp_dict))

    result = {
        'labels': [],
        'data': []
    }

    for month in all_months:
        result['labels'].append(month.strftime('%b %Y'))
        np = profit_dict.get(month, 0) - exp_dict.get(month, 0)
        result['data'].append(np)

    return result


def get_expense_by_category(expenses):
    exp = list(expenses.values(
        'category__name'
    ).annotate(
        total_exp=Sum('amount')
    ).order_by('-total_exp')
    )

    result = {
        'labels': [c['category__name'] for c in exp[:5]],
        'data': [float(e['total_exp']) for e in exp[:5]]  
        }

    result['labels'].append('others')
    result['data'].append(float(sum(e['total_exp'] for e in exp[5:])))

    return result

