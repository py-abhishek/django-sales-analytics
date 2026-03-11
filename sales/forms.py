from django import forms
from django.forms import inlineformset_factory
from .models import Sale, SaleItem, Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email', 'address']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'customer-name', 'placeholder': 'Search or enter new customer'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'id': 'customer-phone', 'placeholder': '9845678325'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'customer-email', 'placeholder': 'email_address@domain.com'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'id': 'customer-address', 'placeholder': 'City, State (Country)'})
        }

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['sale_date', 'payment_method']
        labels = {
            'sale_date': 'Sale Date',
            'payment_method': 'Payment Method'
        }

        widgets = {
            'sale_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'payment_method': forms.Select(attrs={'class': 'form-select'}),
        }
    

class SaleItemForm(forms.ModelForm):
    class Meta:
        model = SaleItem
        fields = ['product', 'quantity']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-select product-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control quantity'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['product'].empty_label = 'Select Product'


        
SaleItemFormSet = inlineformset_factory(
    Sale,
    SaleItem,
    form=SaleItemForm,
    fields=['product', 'quantity'],
    extra=1,
    can_delete=True,
)