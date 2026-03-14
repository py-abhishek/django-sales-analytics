from django.urls import path
from .views import sales_report

urlpatterns = [
    path('sales/',  sales_report.SaleReportView.as_view(), name='sales_report'),
    path('product/',  sales_report.ProductReportView.as_view(), name='product_report'),
    path('revenue-vs-expense/',  sales_report.RevenueExpReportView.as_view(), name='revenue_exp_report'),
    path('inventory/',  sales_report.InventoryReportView.as_view(), name='inventory_report'),
]
