from django.shortcuts import render
from django.views.generic import View

from ..services import inventory_analysis



def get_business_id(request):
    return request.session.get('business_id')

class InventoryReportView(View):
    def get(self, request):

        insights = inventory_analysis.get_insights(get_business_id(request))

        print(insights['low_stock_products'])
        return render(request, 'reports/inventory_report.html', insights)