from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, View
from django.urls import reverse_lazy
from .forms import ProductForm
from .models import Product, ProductCategory
from sales.models import SaleItem

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
        print(product)
        recent_sales = SaleItem.objects.filter(product=product).order_by('-sale.date')
        print(recent_sales[0].sale.customer)

        context = {
            "product": product,
            "recent_sales": recent_sales
        }
        return render(request, "inventory/product_detail.html", context)
        pass