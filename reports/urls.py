from django.urls import path
from . import views

urlpatterns = [
    path('sales/',  views.SaleReportView.as_view(), name='sales_report')
]
