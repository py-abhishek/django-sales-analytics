from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.SalesCreateView.as_view(), name='create_sale'),
    path('view/', views.SalesListView.as_view(), name='sales_list'),
    path('view/<int:pk>', views.SaleDetailView.as_view(), name='sale_detail'),
    path('create/success/<int:pk>', views.SaleSuccessView.as_view(), name='sale_success'),
    path('product-details/<int:id>', views.product_info)
]