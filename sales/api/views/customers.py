
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from sales.models import Customer
from ..serializers import CustomerSerializer


def get_business_id(request):
    return request.session.get('business_id')

# API for customer suggestions and search
class CustomerSearchView(ListAPIView):
    serializer_class = CustomerSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'phone']

    def get_queryset(self):
        queryset = Customer.objects.filter(
            business_id=get_business_id(self.request)
        ).only(
            'id',
            'name',
            'phone',
            'email',
            'address'
        ).order_by('name')
        
        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        query_type = request.query_params.get('type')
        if query_type == 'suggestions':
            queryset = queryset[:10]

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
