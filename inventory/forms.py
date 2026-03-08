from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    '''
    To add new product in the stock
    '''

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['created_at', 'updated_at']

        labels = {
            'name': 'Product Name',
            'sku': 'Unique ID (SKU)',
            'cost_price': 'Cost Price',
            'selling_price': 'Selling Price',
            'stock_quantity': 'Stock Quantity',
            'reorder_level': 'Reorder Level',
            'is_active': 'Is Active'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sku': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit': forms.Select(attrs={'class': 'form-select'}),
            'reorder_level': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

        }

        

