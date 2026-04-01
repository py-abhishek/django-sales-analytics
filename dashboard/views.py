from django.shortcuts import render
from django.views.generic import View

from sales.models import Sale


# Create your views here.

class DashboardView(View):

    def get(self, request):
        business_id = request.session.get('business_id')
        recent_sales = Sale.objects.filter(business_id=business_id).order_by('sale_date')[:5]

        context = {
            'recent_sales': recent_sales 
        }
        return render(request, 'dashboard/dashboard.html', context)