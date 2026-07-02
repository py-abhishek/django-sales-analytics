
from django.views.generic import ListView

from sales.models import Customer


class CustomersListView(ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'customers/customers_list.html'
    ordering = 'name'

    def get_queryset(self):
        return Customer.objects.filter(
            business_id=self.request.session.get('business_id')
            ).only(
                'name', 'phone', 'email', 'address'
            )
    