from django.shortcuts import render
from django.views.generic import View


class RevenueExpReportView(View):
    def get(self, request):
        return render(request, 'reports/revenue_exp_report.html')