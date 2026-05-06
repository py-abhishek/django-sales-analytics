from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddProductView.as_view(), name='add_product'),
    path('categories/', views.ProductCategoryView.as_view(), name='product_categories'),
    path('list/', views.ProductListView.as_view(), name='product_list'),
    path('list/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('add/success/<int:pk>', views.ProductSuccessView.as_view(), name='add_product_success'),
    path('stock-movements/', views.StockMovementListView.as_view(), name='stock_movements'),
    path('edit/<int:pk>', views.EditProductView.as_view(), name='edit_product'),
    path('product-details/<int:id>', views.product_info),
]