from django.urls import path
from . import views

urlpatterns = [
    path('', views.PurchaseView.as_view(), name='add_purchase'),
    path('success/<int:pk>', views.PurchaseSuccessView.as_view(), name='purchase_success'),
    path('view/<int:pk>', views.PurchaseDetailView.as_view(), name='purchase_detail'),
    path('list', views.PurchaseListView.as_view(), name='purchase_list'),
    path('suppliers/search/', views.search_suppliers),
]
