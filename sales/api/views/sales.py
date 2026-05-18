
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from sales.models import Customer, Sale
from inventory.models import Product
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
        ).select_related('customer').order_by('-sale_date')


# Get product info to display pricing
@api_view(['GET'])
def get_product_info(request, id):
    print('get data')
    product = Product.objects.filter(
        id=id,
        business_id=get_business_id(request)
    ).values(
        'selling_price',
        'unit'
    ).first()
    
    if not product:
        return Response(
            {'error': 'Product not found'},
            status=404
        )
    
    product['unit'] = dict(Product.UnitChoices.choices).get(
        product['unit']
    )
    print(product)

    return Response(product)