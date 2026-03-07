from django import forms
from django.forms import inlineformset_factory
from .models import Sale, SaleItem

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ["customer", "sale_date", "payment_method"]
        labels = {
            'sale_date': 'Sale Date',
            'payment_method': 'Payment Method'
        }

        widgets = {
            "customer": forms.Select(attrs={"class": "form-select"}),
            "sale_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "payment_method": forms.Select(attrs={"class": "form-select"}),
        }

class SaleItemForm(forms.ModelForm):
    class Meta:
        model = SaleItem
        fields = ["product", "quantity"]
        widgets = {
            "product": forms.Select(attrs={"class": "form-select"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
        }

        
SaleItemFormSet = inlineformset_factory(
    Sale,
    SaleItem,
    form=SaleItemForm,
    fields=["product", "quantity"],
    extra=2,
    can_delete=True,
)