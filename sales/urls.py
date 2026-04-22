from django.urls import path
from .views import sales, customers

urlpatterns = [
    path('create/', sales.SalesCreateView.as_view(), name='create_sale'),
    path('view/', sales.SalesListView.as_view(), name='sales_list'),
    path('view/<int:pk>', sales.SaleDetailView.as_view(), name='sale_detail'),
    path('view/cancel/<int:sale_id>', sales.CancelSaleView.as_view(), name='cancel_sale'),
    path('create/success/<int:pk>', sales.SaleSuccessView.as_view(), name='sale_success'),

    path('customers/list/', customers.CustomersListView.as_view(), name='customers_list'),

    # path('api/sales', sales.search_sales)

]