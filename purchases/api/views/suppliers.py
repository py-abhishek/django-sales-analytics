
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from purchases.models import Supplier
from ..serializers import SupplierSerializer


def get_business_id(request):
    return request.session.get('business_id')

# API for supplier suggestions and search
class SupplierSearchView(ListAPIView):
    serializer_class = SupplierSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'phone']

    def get_queryset(self):
        return Supplier.objects.filter(
            business_id=get_business_id(self.request)
        ).order_by('name')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        query_type = request.query_params.get('type')
        if query_type == 'suggestions':
            queryset = queryset[:10]

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    