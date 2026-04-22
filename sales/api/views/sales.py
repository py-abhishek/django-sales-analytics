
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from django.db.models import Q

from sales.models import Customer, Sale
from ..serializers import CustomerSerializer, SaleSerializer


def get_business_id(request):
    return request.session.get('business_id')


# For sales List (History)
class SalesSearchView(ListAPIView):
    serializer_class = SaleSerializer
    filter_backends = [SearchFilter]
    search_fields = ['customer__name']

    def get_queryset(self):
        return Sale.objects.filter(
            business_id=get_business_id(self.request)
        ).order_by('-sale_date')
    