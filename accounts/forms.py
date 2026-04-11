from django.forms import ModelForm
from django import forms

from .models import User

class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
        }

class SignInForm(ModelForm):
    class Meta:
        model = User
        fields = ['email']

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
        }
        

        