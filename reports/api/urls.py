from django.urls import path
from . import views

urlpatterns = [
    path('sales-report/', views.SalesReportView.as_view()),
    path('product-report/', views.ProductReportView.as_view()),
    path('rev-exp-report/', views.RevExpReport.as_view()),
    path('inventory-report/', views.InventoryReportView.as_view()),
]
