
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

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
        queryset = Supplier.objects.filter(
            business_id=get_business_id(self.request)
        ).order_by('name')

        query_type = self.request.query_params.get('type', 'search')

        if query_type == 'suggestions':
            return queryset[:10]
    
        return queryset


    