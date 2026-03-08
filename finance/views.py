from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Expense, ExpenseCategory
from .forms import AddExpenseForm

# Create your views here.

class AddExpenseView(CreateView):
    model = Expense
    form_class = AddExpenseForm
    template_name = 'expense/add_expense.html'
    success_url = reverse_lazy('expense_success')

class ExpenseListView(ListView):
    model = Expense
    template_name = 'expense/expense_list.html'
    context_object_name = 'expenses'
    ordering = '-expense_date'


class ExpenseDetailView(DetailView):
    model = Expense
    context_object_name = 'expense'
    template_name = 'expense/expense_detail.html'

class ExpenseCategoryView(ListView):
    model = ExpenseCategory
    template_name = 'expense/expense_categories.html'
    context_object_name = 'categories'
    ordering = 'name'
