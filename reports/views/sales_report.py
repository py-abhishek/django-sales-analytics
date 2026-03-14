from django.shortcuts import render
from django.views.generic import View
from sales.models import Sale, Customer
from ..services import sales_analysis

# Create your views here.


class SaleReportView(View):
    def get(self, request):
        sales = Sale.objects.all().order_by('-sale_date')
        cutomers = Customer.objects.all().order_by('name')

        sales_insights = sales_analysis.get_insights(sales)
        
        context = {
            'sales': sales,
            'customers': cutomers
        }

        context.update(sales_insights)
        return render(request, 'reports/sales_report.html', context)
    

class ProductReportView(View):
    def get(self, request):
        return render(request, 'reports/product_report.html')
    
class RevenueExpReportView(View):
    def get(self, request):
        return render(request, 'reports/revenue_exp_report.html')
    
class InventoryReportView(View):
    def get(self, request):
        return render(request, 'reports/inventory_report.html')