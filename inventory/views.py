from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, View
from django.urls import reverse_lazy
from django.utils.timezone import now
from .forms import ProductForm
from .models import Product, ProductCategory
from sales.models import SaleItem
from . import services

# Create your views here.


class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "inventory/add_product.html"
    success_url = reverse_lazy("add_product_success")

class ProductCategoryView(ListView):
    model = ProductCategory
    template_name = "inventory/product_categories.html"
    context_object_name = "categories"
    ordering = "name"


class ProductListView(ListView):
    model = Product
    template_name = "inventory/product_list.html"
    context_object_name = "products"
    ordering = "-created_at"

class ProductDetailView(View):
    def get(self, request, pk):
        product_id = pk
        product = Product.objects.get(id=product_id)
        current_year = now().year
        all_sales = SaleItem.objects.filter(product=product, sale__sale_date__year=current_year).order_by('-sale__sale_date')
        recent_sales = all_sales[:5]

        sales_insights = services.get_sales_insights(all_sales)

        context = {
            "product": product,
            "recent_sales": recent_sales,
            "last_sold_date": recent_sales.first().sale.sale_date if recent_sales else None,
            "current_year": current_year
        }

        context |= sales_insights

        return render(request, "inventory/product_detail.html", context)
        