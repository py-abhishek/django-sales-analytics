from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddProductView.as_view(), name='add_product'),
    path('categories/', views.ProductCategoryView.as_view(), name='product_categories'),
    path('list/', views.ProductListView.as_view(), name='product_list'),
    path('list/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('success/', views.AddProductView.as_view(), name='add_product_success'),
    path('stock-movements/', views.StockMovementListView.as_view(), name='stock_movements'),
    path('product-details/<int:id>', views.product_info),
]