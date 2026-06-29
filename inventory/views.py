from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, View, DetailView, UpdateView
from django.urls import reverse_lazy, reverse
from django.utils.timezone import now
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .forms import ProductForm, ProductCategoryForm, UpdateProductForm
from .models import Product, ProductCategory, InventoryLedger
from sales.models.sales import SaleItem
from . import services
from inventory.services import new_product_ledger
import math

from core.permissions.mixins import RoleRequiredMixin
from business.models import Membership

from django.contrib import messages


def get_business_id(request):
    return request.session.get('business_id')

# Create your views here.

# create new product
class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/add_product.html'

    def get_success_url(self):
        return reverse('add_product_success', args=[self.object.pk])

    def form_valid(self, form):
        request = self.request
        form.instance.business_id = get_business_id(request)
        form.instance.created_by = request.user

        response = super().form_valid(form)

        product = self.object
        sku = request.POST.get('sku')
        unit_cost = request.POST.get('current_avg_cost')
        quantity = request.POST.get('current_stock')
        total_cost = int(quantity)*int(unit_cost)

        # Create new product ledger
        new_product_ledger(
            product,
            quantity,
            unit_cost,
            total_cost,
            get_business_id(request)
        )

        return response
    

# Manage and create product category
class ProductCategoryView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = 'inventory/product_categories.html'
    success_url = reverse_lazy('product_categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = ProductCategory.objects.filter(business_id=get_business_id(self.request)).order_by('-created_at')
        return context
    
    def form_valid(self, form):
        form.instance.business_id = get_business_id(self.request)
        return super().form_valid(form)
    
    

# View all products
class ProductListView(ListView):
    model = Product
    template_name = 'inventory/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(business_id=get_business_id(self.request)).order_by('-created_at')


# View a particuler product in detail
class ProductDetailView(View):
    def get(self, request, pk):
        business_id = get_business_id(request)

        product = get_object_or_404(Product.objects.select_related('category'), id=pk)
        current_year = now().year
        all_sales = SaleItem.objects.filter(business_id=business_id, product=product, sale__sale_date__year__gte=current_year).select_related('product', 'sale', 'sale__customer').order_by('-sale__sale_date')
        recent_sales = all_sales[:5]

        sales_insights = services.get_sales_insights(all_sales, business_id)

        context = {
            'product': product,
            'recent_sales': recent_sales,
            'last_sold_date': recent_sales[0].sale.sale_date if recent_sales else None,
            'current_year': current_year
        }

        context.update(sales_insights)

        return render(request, 'inventory/product_detail.html', context)
    

# View all stock changes
class StockMovementListView(ListView):
    model = InventoryLedger
    template_name = 'inventory/stock_movements_list.html'
    context_object_name = 'stock_movements'
    
    def get_queryset(self):
        return InventoryLedger.objects.filter(
            business_id=get_business_id(self.request)
            ).select_related('product').order_by('-created_at')[:100]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_pages"] = math.ceil(InventoryLedger.objects.filter(business_id=get_business_id(self.request)).count()/100)
        return context
    

# Product success view
class ProductSuccessView(DetailView):
    model = Product
    template_name = 'inventory/product_success.html'
    context_object_name = 'product'

    def get_queryset(self):
        return Product.objects.filter(business_id=get_business_id(self.request))
    
# Edit product view
class EditProductView(RoleRequiredMixin, UpdateView):
    allowed_roles = [Membership.UserRoleChoices.ADMIN]
    permission_denied_url = 'product_detail'

    model = Product
    form_class = UpdateProductForm
    template_name = 'inventory/edit_product.html'

    def get_queryset(self):
        return Product.objects.filter(business_id=get_business_id(self.request))
    
    def get_success_url(self):
        messages.success(self.request, 'Product updated successfully.')
        return reverse('product_detail', kwargs={'pk': self.object.pk})
    
    


# API - get product info
def product_info(request, id):
    product = get_object_or_404(Product, id=id, business_id=get_business_id(request))

    product_info ={
        'selling_price': product.selling_price,
        'unit': product.get_unit_display()
    }

    return JsonResponse(product_info)