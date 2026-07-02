from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, View

from purchases.models import Supplier


def get_business_id(request):
    return request.session.get('business_id')

class SuppliersListView(ListView):
    model = Supplier
    context_object_name = 'suppliers'
    template_name = 'suppliers/suppliers_list.html'
    ordering = 'name'

    def get_queryset(self):
        queryset = Supplier.objects.filter(business_id=get_business_id(self.request)).only(
            'name', 'phone', 'email', 'address'
        )

        return queryset
    