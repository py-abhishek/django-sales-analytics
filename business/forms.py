from django.forms import ModelForm
from django import forms
from .models import Business, Membership

class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = '__all__'
        exclude = ['created_by', 'is_active', 'created_at', 'updated_at']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter business name'}),
            'business_type': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter business phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter business email'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter business address'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['business_type'].choices = [('', 'Select business type')] + list(self.fields['business_type'].choices)