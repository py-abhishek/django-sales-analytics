
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from django.db.models import Q

from inventory.models import Product, InventoryLedger, ProductCategory
from .serializers import ProductSerializer, InventoryLedgerSerializer, ProductCategorySerializer


def get_business_id(request):
    return request.session.get('business_id')

# Search products
class ProductsSearchView(ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        queryset = Product.objects.filter(
            business_id=get_business_id(self.request)
        ).order_by('name')
        
        return queryset
    
# Search Product categories
class ProductCategoriesSearchView(ListAPIView):
    serializer_class = ProductCategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        return ProductCategory.objects.filter(
            business_id=get_business_id(self.request)
        ).order_by('-created_at')


# For Stock Movements
class LedgerSearchView(ListAPIView):
    serializer_class = InventoryLedgerSerializer
    filter_backends = [SearchFilter]
    search_fields = ['product__name']

    def get_queryset(self):
        return InventoryLedger.objects.filter(
            business_id=get_business_id(self.request)
        ).order_by('-created_at')
    