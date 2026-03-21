from django.shortcuts import render
from django.views.generic import View

from ..services import inventory_analysis


class InventoryReportView(View):
    def get(self, request):

        insights = inventory_analysis.get_insights()

        print(insights['low_stock_products'])
        return render(request, 'reports/inventory_report.html', insights)