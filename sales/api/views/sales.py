
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from sales.models import Customer, Sale
from ..serializers import CustomerSerializer, SaleSerializer


def get_business_id(request):
    return request.session.get('business_id')


# For sales List (History)
class SalesSearchView(ListAPIView):
    serializer_class = SaleSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['customer__name']

    filterset_fields = ['sale_date']

    def get_queryset(self):
        return Sale.objects.filter(
            business_id=get_business_id(self.request)
        ).order_by('-sale_date')
    