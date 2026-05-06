from django.urls import path
from . import views

urlpatterns = [
    path('search-products/', views.ProductsSearchView.as_view()),
    path('search-movements/', views.LedgerSearchView.as_view()),
    path('search-product-categories/', views.ProductCategoriesSearchView.as_view()),
    path('stock-movements/', views.LedgerListView.as_view()),
]
