from django.shortcuts import render, redirect
from django.db import transaction
from django.views.generic import ListView, DetailView
from django.views import View
from django.urls import reverse_lazy

from .forms import SaleForm, SaleItemFormSet
from .models import Sale
from . import services

import logging
logger = logging.getLogger(__name__)

# Create your views here.


class SalesCreateView(View):
    """
    To handle the request of creating a new sale
    """

    def get(self, request):
        form = SaleForm()
        formset = SaleItemFormSet()
        return render(request, "sales/create_sale.html", {
            'form': form,
            'formset': formset
        })

    def post(self, request):
        form = SaleForm(request.POST)
        formset = SaleItemFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            form_data = form.cleaned_data
            formset_data = formset.cleaned_data

            try:
                """
                Calling function from services to validate and create sale
                """
                services.create_sale(
                    form_data["customer"],
                    form_data["sale_date"],
                    form_data["payment_method"],
                    formset_data
                )
                return redirect(reverse_lazy("sale_success"))
            except Exception as e:
                logger.error(e)
                form.add_error(None, str(e))

        return render(request, "sales/create_sale.html", {
            'form': form,
            'formset': formset
        })
    

class SalesListView(ListView):
    model = Sale
    template_name = "sales/sales_list.html"
    context_object_name = "sales"
    ordering = ["-sale_date"]
        
class SaleDetailView(DetailView):
    model = Sale
    template_name = "sales/sale_detail.html"
    context_object_name = "sale"
    print("hello")
    