from django.urls import path
from .views import sales_report, product_report, revenue_exp_report, inventory_report

urlpatterns = [
    path('sales/',  sales_report.SaleReportView.as_view(), name='sales_report'),
    path('product/',  product_report.ProductReportView.as_view(), name='product_report'),
    path('revenue-vs-expense/',  revenue_exp_report.RevenueExpReportView.as_view(), name='revenue_exp_report'),
    path('inventory/',  inventory_report.InventoryReportView.as_view(), name='inventory_report'),

    # API
    path('product/filter-data', product_report.get_filtered_data)
]
