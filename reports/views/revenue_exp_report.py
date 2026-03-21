from django.shortcuts import render
from django.views.generic import View

from ..services import revenue_exp_analysis


class RevenueExpReportView(View):
    def get(self, request):

        insights = revenue_exp_analysis.get_insights()

        return render(request, 'reports/revenue_exp_report.html', insights)