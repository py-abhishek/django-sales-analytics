from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, View
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .forms import ProductForm, ProductCategoryForm
from .models import Product, ProductCategory, InventoryLedger
from sales.models import SaleItem
from . import services

# Create your views here.


class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/add_product.html'
    success_url = reverse_lazy('add_product_success')

class ProductCategoryView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = 'inventory/product_categories.html'
    success_url = reverse_lazy('product_categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = ProductCategory.objects.all().order_by('-created_at')
        return context
    


class ProductListView(ListView):
    model = Product
    template_name = 'inventory/product_list.html'
    context_object_name = 'products'
    ordering = '-created_at'

class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        current_year = now().year
        all_sales = SaleItem.objects.filter(product=product, sale__sale_date__year__gte=current_year).select_related('sale').order_by('-sale__sale_date')
        recent_sales = all_sales[:5]

        sales_insights = services.get_sales_insights(all_sales)

        context = {
            'product': product,
            'recent_sales': recent_sales,
            'last_sold_date': recent_sales[0].sale.sale_date if recent_sales else None,
            'current_year': current_year
        }

        context.update(sales_insights)

        return render(request, 'inventory/product_detail.html', context)
    

class StockMovementListView(ListView):
    model = InventoryLedger
    template_name = 'inventory/stock_movements_list.html'
    context_object_name = 'stock_movements'
    ordering = '-created_at'


# API
def product_info(request, id):
    product = get_object_or_404(Product, id=id)

    product_info ={
        'selling_price': product.selling_price,
        'unit': product.get_unit_display()
    }

    return JsonResponse(product_info)