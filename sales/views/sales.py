from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import View
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.db.models import Q, Prefetch

from ..forms import SaleForm, SaleItemFormSet, CustomerForm
from sales.models import Sale, SaleItem
from inventory.models import Product
from .. import services
from business.models import Membership

from core.permissions.mixins import RoleRequiredMixin

from rest_framework.decorators import api_view
from rest_framework.response import Response

import logging
logger = logging.getLogger(__name__)



def get_business_id(request):
    return request.session.get('business_id')

# Create your views here.

# Create new sale
class SalesCreateView(View):

    def get(self, request):
        sale_form = SaleForm(prefix='sale')
        customer_form = CustomerForm(prefix='customer')

        products =list(
            Product.objects.filter(
                business_id=get_business_id(request)
            ).only(
                'id',
                'name'
            )
        )
        

        formset = SaleItemFormSet(
            form_kwargs={'products': products}
        )

        return render(request, 'sales/create_sale.html', {
            'customer_form': customer_form,
            'sale_form': sale_form,
            'formset': formset
        })

    def post(self, request):

        customer_form = CustomerForm(request.POST, prefix='customer')
        sale_form = SaleForm(request.POST, prefix='sale')

        products =list(
            Product.objects.filter(
                business_id=get_business_id(request)
            ).only(
                'id',
                'name'
            )
        )

        formset = SaleItemFormSet(
            request.POST,
            form_kwargs={'products': products}
            )
        row_customer_id = request.POST.get('customer_id')

        if row_customer_id.isdigit():
            customer_id = int(row_customer_id)
        else: 
            customer_id = None

        is_new_customer = False

        if not customer_id:
            # New Customer
            is_new_customer = True


        # logger.info(customer_form)

        is_customer_form_valid = True

        if is_new_customer:
            is_customer_form_valid = customer_form.is_valid()

        if sale_form.is_valid() and formset.is_valid() and is_customer_form_valid:
            customer_form_data = customer_form.cleaned_data if is_new_customer else None
            sale_form_data = sale_form.cleaned_data
            formset_data = formset.cleaned_data

            try:
                '''
                Calling function from services to validate and create sale
                '''
                saved_sale = services.create_sale(
                    customer_id,
                    is_new_customer,
                    customer_form_data,
                    sale_form_data,
                    formset_data,
                    get_business_id(request),
                    request.user
                )
                logger.info('saved data %s', saved_sale)
                return redirect(reverse_lazy('sale_success', kwargs={'pk':saved_sale.id}))
            except Exception as e:
                logger.error(e)
                sale_form.add_error(None, e)

        logger.info("Error while creating sale")
        return render(request, 'sales/create_sale.html', {
            
            'customer_form': customer_form,
            'sale_form': sale_form,
            'formset': formset
        })
    

# View sales history
class SalesListView(ListView):
    model = Sale
    template_name = 'sales/sales_list.html'
    context_object_name = 'sales'
    
    def get_queryset(self):
        return Sale.objects.filter(
            business_id=get_business_id(self.request)
            ).select_related(
                'customer',
                'business',
                'created_by'
            ).order_by('-sale_date')
        

# View a particuler sale detail
class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sales/sale_detail.html'
    context_object_name = 'sale'
    
    def get_queryset(self):
        return Sale.objects.filter(
            business_id=get_business_id(self.request)
            ).select_related(
                'customer',
                'business',
                'created_by'
            ).prefetch_related(
                Prefetch(
                    'items',
                    queryset=SaleItem.objects.select_related('product')
                )
            )

# Render success template on successfull sale
class SaleSuccessView(DetailView):
    model = Sale
    template_name = 'sales/sale_success.html'
    context_object_name = 'sale'
    
    def get_queryset(self):
        return Sale.objects.filter(
            business_id=get_business_id(self.request)
            ).select_related(
                'customer',
                'business',
                'created_by'
            ).prefetch_related(
                Prefetch(
                    'items',
                    queryset=SaleItem.objects.select_related('product')
                )
            )


# Cancel sale
class CancelSaleView(RoleRequiredMixin, View):
    allowed_roles = [Membership.UserRoleChoices.ADMIN]

    def post(self, request, sale_id):
        services.cancel_sale(request, sale_id, request.session.get('business_id'))

        return redirect('sale_detail', sale_id)

