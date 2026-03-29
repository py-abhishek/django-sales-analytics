from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Expense, ExpenseCategory
from .forms import ExpenseForm, ExpenseCategoryForm

# Create your views here.

# Create new expense
class AddExpenseView(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expense/add_expense.html'
    success_url = reverse_lazy('expense_success')

# View all expenses
class ExpenseListView(ListView):
    model = Expense
    template_name = 'expense/expense_list.html'
    context_object_name = 'expenses'
    ordering = '-expense_date'

# View a particuler expense in detail
class ExpenseDetailView(DetailView):
    model = Expense
    context_object_name = 'expense'
    template_name = 'expense/expense_detail.html'

# Manage and create expense categories
class ExpenseCategoryView(CreateView):
    model = ExpenseCategory
    form_class = ExpenseCategoryForm
    template_name = 'expense/expense_categories.html'
    success_url = reverse_lazy('expense_categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ExpenseCategory.objects.all().order_by('-created_at')
        return context
    


