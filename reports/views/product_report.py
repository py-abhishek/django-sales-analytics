from django.shortcuts import render
from django.views.generic import View

from inventory.models import ProductCategory
from ..services import product_analysis 



def get_business_id(request):
    return request.session.get('business_id')

class ProductReportView(View):
    def get(self, request):
        business_id = get_business_id(self.request)
        product_categories = ProductCategory.objects.filter(business_id=business_id).order_by('name')

        # calling function from services layer
        insights = product_analysis.get_insights(business_id)

        context = {
            'product_categories': product_categories
        }

        context.update(insights)

        return render(request, 'reports/product_report.html', context)
    
