from django.urls import path
from .views import purchases, suppliers

urlpatterns = [
    path('', purchases.PurchaseView.as_view(), name='add_purchase'),
    path('success/<int:pk>', purchases.PurchaseSuccessView.as_view(), name='purchase_success'),
    path('view/<int:pk>', purchases.PurchaseDetailView.as_view(), name='purchase_detail'),
    path('list', purchases.PurchaseListView.as_view(), name='purchases_list'),

    path('suppliers', suppliers.SuppliersListView.as_view(), name='suppliers_list'),
]
