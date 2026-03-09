from django import forms
from django.forms import inlineformset_factory
from .models import Sale, SaleItem, Customer

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer', 'sale_date', 'payment_method']
        labels = {
            'sale_date': 'Sale Date',
            'payment_method': 'Payment Method'
        }

        widgets = {
            'customer': forms.Select(attrs={'class': 'form-select'}),
            'sale_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'payment_method': forms.Select(attrs={'class': 'form-select'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['customer'].empty_label = 'Select Customer'

        """
        try:
            walkin = Customer.objects.get(is_walkin=True)
            self.fields['customer'].initial = walkin
        except Exception as e:
            pass
        """
    

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