from django import forms
from django.forms import inlineformset_factory
from .models import Purchase, PurchaseItem, Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'phone', 'email', 'address']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'supplier-name', 'placeholder': 'Search or add new supplier'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'id': 'supplier-phone', 'placeholder': '10 digits mobile'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'supplier-email', 'placeholder': 'Email (optional)'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'id': 'supplier-address', 'placeholder': 'Address (optional)'})
        }

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['purchase_date', 'payment_method']
        labels = {
            'purchase_date': 'purchase Date',
            'payment_method': 'Payment Method'
        }

        widgets = {
            'purchase_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'payment_method': forms.Select(attrs={'class': 'form-select'}),
        }
    

class PurchaseItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseItem
        fields = ['product', 'quantity']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-select product-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control quantity'}),
            'unit_cost': forms.NumberInput(attrs={'class': 'form-control cost'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['product'].empty_label = 'Choose Product'


        
PurchaseItemFormSet = inlineformset_factory(
    Purchase,
    PurchaseItem,
    form=PurchaseItemForm,
    fields=['product', 'quantity', 'unit_cost'],
    extra=1,
    can_delete=True,
)