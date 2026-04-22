from django.shortcuts import render
from django.views.generic import View
from sales.models import Sale, Customer
from ..services import sales_analysis



def get_business_id(request):
    return request.session.get('business_id')

# Create your views here.

class SaleReportView(View):
    def get(self, request):
        business_id = get_business_id(request)
        sales = Sale.objects.filter(business_id=business_id, status=Sale.StatusChoices.COMPLETED).order_by('-sale_date')
        cutomers = Customer.objects.filter(business_id=business_id).order_by('name')

        sales_insights = sales_analysis.get_insights(sales, business_id)
        
        context = {
            'sales': sales,
            'customers': cutomers
        }

        context.update(sales_insights)
        return render(request, 'reports/sales_report.html', context)