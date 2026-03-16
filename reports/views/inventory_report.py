from django.shortcuts import render
from django.views.generic import View


class InventoryReportView(View):
    def get(self, request):
        return render(request, 'reports/inventory_report.html')