from django.urls import path
from . import views

urlpatterns = [
    path('search-suppliers/', views.SupplierSearchView.as_view()),
    path('search-purchases/', views.PurchasesSearchView.as_view()),
]
