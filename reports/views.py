from django.shortcuts import render
from django.views.generic import View
from sales.models import Sale, Customer
from . import services

# Create your views here.


class SaleReportView(View):
    def get(self, request):
        sales = Sale.objects.all().order_by('-sale_date')
        cutomers = Customer.objects.all().order_by('name')

        sales_insights = services.get_insights(sales)

        context = {
            'sales': sales,
            'customers': cutomers
        }

        context.update(sales_insights)
        return render(request, 'reports/sales_report.html', context)