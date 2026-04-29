from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import timedelta
from django.utils.timezone import now

from reports.services import inventory_analysis


class InventoryReportView(APIView):
    def get(self, request):
        business_id = business_id=request.session.get('business_id')

        category_id = request.GET.get('category')
        product_id = request.GET.get('product')

        if category_id:
            category_id = int(category_id)
        
        if product_id:
            product_id = int(product_id)


        try:
            data = inventory_analysis.get_insights(
                business_id=business_id,
                category_id=category_id,
                product_id=product_id
                )
        except Exception as e:
            print(e)
            data = {'error': e}

        return Response(data)
    