from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, DetailView, ListView
from logging import Logger
from django.http import JsonResponse
from django.db.models import Q

from ..forms import PurchaseForm, SupplierForm, PurchaseItemFormSet
from .. import services
from ..models import Purchase, Supplier

import logging
logger = logging.getLogger(__name__)



def get_business_id(request):
    return request.session.get('business_id')

# Create your views here.
# Create new purchase
class PurchaseView(View):
    def get(self, request):
        purchase_form = PurchaseForm(prefix='purchase')
        supplier_form = SupplierForm(prefix='supplier')
        formset = PurchaseItemFormSet()
        return render(request, 'purchase/add_purchase.html', {
            'supplier_form': supplier_form,
            'purchase_form': purchase_form,
            'formset': formset
        })

    def post(self, request):
        
        supplier_form = SupplierForm(request.POST, prefix='supplier')
        purchase_form = PurchaseForm(request.POST, prefix='purchase')
        formset = PurchaseItemFormSet(request.POST)
        raw_supplier_id = request.POST.get('supplier_id')

        if raw_supplier_id.isdigit():
            supplier_id = int(raw_supplier_id)
        else: 
            supplier_id = None

        is_new_supplier = False

        if not supplier_id:
            # New supplier
            is_new_supplier = True

        # logger.info(supplier_form)

        is_supplier_form_valid = True

        if is_new_supplier:
            is_supplier_form_valid = supplier_form.is_valid()

        if purchase_form.is_valid() and formset.is_valid() and is_supplier_form_valid:
            logger.info("Hello")
            supplier_form_data = supplier_form.cleaned_data if is_new_supplier else None
            purchase_form_data = purchase_form.cleaned_data
            formset_data = formset.cleaned_data

            try:
                saved_purchase = services.create_purchase(
                    supplier_id,
                    is_new_supplier,
                    supplier_form_data,
                    purchase_form_data,
                    formset_data,
                    get_business_id(request)
                )
                logger.info('saved data %s', saved_purchase)
                return redirect(reverse_lazy('purchase_success', kwargs={'pk':saved_purchase.id}))
            except Exception as e:
                logger.error(e)
                purchase_form.add_error(None, e)

        logger.info("Error while creating purchase")
        return render(request, 'purchase/add_purchase.html', {
            
            'supplier_form': supplier_form,
            'purchase_form': purchase_form,
            'formset': formset
        })
    

# Render success template
class PurchaseSuccessView(DetailView):
    model = Purchase
    template_name = 'purchase/purchase_success.html'
    context_object_name = 'purchase'
    
    def get_queryset(self):
        return Purchase.objects.filter(business_id=get_business_id(self.request))


# View purchase history
class PurchaseListView(ListView):
    
    model = Purchase
    template_name = 'purchase/purchase_list.html'
    context_object_name = 'purchases'

    def get_queryset(self):
        return Purchase.objects.filter(business_id=get_business_id(self.request)).order_by('-purchase_date')



# View a particuler product details
class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = 'purchase/purchase_detail.html'
    context_object_name = 'purchase'

    def get_queryset(self):
        return Purchase.objects.filter(business_id=get_business_id(self.request))
