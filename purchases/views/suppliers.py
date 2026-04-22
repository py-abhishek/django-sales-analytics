from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, View

from purchases.models import Supplier


class SuppliersListView(ListView):
    model = Supplier
    context_object_name = 'suppliers'
    template_name = 'suppliers/suppliers_list.html'
    ordering = 'name'