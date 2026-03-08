from django.shortcuts import render
from django.views.generic import View
from sales.models import Sale, SaleItem

# Create your views here.

class DashboardView(View):
    def get(self, request):
        recent_sales = Sale.objects.all().order_by('sale_date')[:5]
        print(recent_sales)

        context = {
            'recent_sales': recent_sales 
        }
        return render(request, 'dashboard/dashboard.html', context)