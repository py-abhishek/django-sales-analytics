from django.shortcuts import render
from django.views.generic import View

from sales.models import Sale
from .services import get_insights
from django.contrib import messages


# Create your views here.

class DashboardView(View):

    def get(self, request):

        business_id = request.session.get('business_id')
        recent_sales = Sale.objects.filter(business_id=business_id).order_by('sale_date')[:5]

        insights = get_insights(business_id)

        context = {
            'recent_sales': recent_sales 
        }

        context.update(insights)
        
        return render(request, 'dashboard/dashboard.html', context)