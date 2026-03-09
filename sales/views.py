from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.views.generic import ListView, DetailView
from django.views import View
from django.urls import reverse_lazy
from django.http import JsonResponse

from .forms import SaleForm, SaleItemFormSet
from .models import Sale
from inventory.models import Product
from . import services

import logging
logger = logging.getLogger(__name__)

# Create your views here.


class SalesCreateView(View):

    def get(self, request):
        form = SaleForm()
        formset = SaleItemFormSet()
        return render(request, 'sales/create_sale.html', {
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
                '''
                Calling function from services to validate and create sale
                '''
                saved_sale = services.create_sale(
                    form_data['customer'],
                    form_data['sale_date'],
                    form_data['payment_method'],
                    formset_data
                )
                return redirect(reverse_lazy('sale_success', kwargs={'pk':saved_sale.id}))
            except Exception as e:
                logger.error(e)
                form.add_error(None, str(e))

        return render(request, 'sales/create_sale.html', {
            'form': form,
            'formset': formset
        })
    

class SalesListView(ListView):
    model = Sale
    template_name = 'sales/sales_list.html'
    context_object_name = 'sales'
    ordering = ['-sale_date']
        
class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sales/sale_detail.html'
    context_object_name = 'sale'


class SaleSuccessView(DetailView):
    model = Sale
    template_name = 'sales/sale_success.html'
    context_object_name = 'sale'



# APIs
def product_info(request, id):
    product = get_object_or_404(Product, id=id)

    product_info ={
        'selling_price': product.selling_price,
        'unit': product.get_unit_display()
    }

    return JsonResponse(product_info)