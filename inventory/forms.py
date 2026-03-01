from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    """
    To add new product in the stock
    """

    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['is_active', 'created_at', 'updated_at']


