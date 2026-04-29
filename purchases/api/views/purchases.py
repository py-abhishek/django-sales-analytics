
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from purchases.models import Purchase
from ..serializers import PurchaseSerializer


def get_business_id(request):
    return request.session.get('business_id')


# For purchase list (History)
class PurchasesSearchView(ListAPIView):
    serializer_class = PurchaseSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['supplier__name']

    filterset_fields = ['purchase_date']

    def get_queryset(self):
        return Purchase.objects.filter(
            business_id=get_business_id(self.request)
        ).order_by('-purchase_date')
    
    
    