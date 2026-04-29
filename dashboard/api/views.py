from rest_framework.views import APIView
from rest_framework.response import Response

from dashboard import services


class DashboardView(APIView):
    def get(self, request):
        business_id = request.session.get('business_id')
        year = request.GET.get('year')
        # month = request.GET.get('month')

        if year:
            year = int(year)
        # if month:
        #     month = int(month)

        insights = services.get_insights(business_id, year)

        context = {}
        context.update(insights)

        return Response(context)
