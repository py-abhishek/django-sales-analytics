from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import timedelta
from django.utils.timezone import now

from reports.services import sales_analysis


class SalesReportView(APIView):
    def get(self, request):
        business_id = business_id=request.session.get('business_id')

        date = request.GET.get('date')
        customer_id = request.GET.get('customer')
        p_method = request.GET.get('pmethod')

        if customer_id:
            customer_id = int(customer_id)

        # Validate date
        from_date = self.validate_date(date)

        try:
            data = sales_analysis.get_insights(
                business_id=business_id,
                from_date=from_date,
                customer_id=customer_id,
                p_method=p_method
                )
        except Exception as e:
            print(e)
            data = {'error': e}

        return Response(data)
    
    def validate_date(self, date):
        today = now()

        if date == '6m':
            from_date = today - timedelta(days=180)
        
        elif date == '1y':
            from_date = today - timedelta(days=365)
        
        elif date == '2y':
            from_date = today - timedelta(days=730)
        
        else:
            from_date = None
        
        return from_date