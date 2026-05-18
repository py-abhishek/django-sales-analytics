from django import forms
from .models import Expense, ExpenseCategory


class ExpenseCategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-select', 'rows': '3'}),

        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        exclude = ['created_by', 'business', 'updated_at', 'created_at']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control exp-dsc', 'rows': '3'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'expense_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})

        }