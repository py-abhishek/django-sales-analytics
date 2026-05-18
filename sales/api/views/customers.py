
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

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

        query_type = self.request.query_params.get('type', 'search')

        if query_type == 'suggestions':
            return queryset[:10]
        
        return queryset
