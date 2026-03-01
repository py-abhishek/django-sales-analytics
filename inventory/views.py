from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import ProductForm
from .models import Product

# Create your views here.


class AddProductView(CreateView):
    """
    To handle product form,
    we're using to add new products in the stock
    """

    model = Product
    form_class = ProductForm
    template_name = "inventory/index.html"
    success_url = "/success"

