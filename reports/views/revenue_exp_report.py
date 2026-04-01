from django.shortcuts import render
from django.views.generic import View

from ..services import revenue_exp_analysis


def get_business_id(request):
    return request.session.get('business_id')

class RevenueExpReportView(View):
    def get(self, request):

        insights = revenue_exp_analysis.get_insights(get_business_id(request))

        return render(request, 'reports/revenue_exp_report.html', insights)