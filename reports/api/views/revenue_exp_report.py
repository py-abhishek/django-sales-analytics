from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import timedelta
from django.utils.timezone import now

from reports.services import revenue_exp_analysis


class RevExpReport(APIView):
    def get(self, request):
        business_id = business_id=request.session.get('business_id')

        date = request.GET.get('date')

        # Validate date
        from_date = self.validate_date(date)

        try:
            data = revenue_exp_analysis.get_insights(
                business_id=business_id,
                from_date=from_date
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