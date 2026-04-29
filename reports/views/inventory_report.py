from django.shortcuts import render
from django.views.generic import View

from ..services import inventory_analysis
from inventory.models import Product, ProductCategory



def get_business_id(request):
    return request.session.get('business_id')

class InventoryReportView(View):
    def get(self, request):

        insights = inventory_analysis.get_insights(get_business_id(request))
        categories = ProductCategory.objects.filter(business_id=get_business_id(request))
        products = Product.objects.filter(business_id=get_business_id(request))

        context = {
            'categories': categories,
            'products': products
        }

        context.update(insights)

        return render(request, 'reports/inventory_report.html', context)