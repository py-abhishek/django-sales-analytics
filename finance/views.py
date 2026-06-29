from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy, reverse
from .models import Expense, ExpenseCategory
from .forms import ExpenseForm, ExpenseCategoryForm



def get_business_id(request):
    return request.session.get('business_id')

# Create your views here.

# Create new expense
class AddExpenseView(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expense/add_expense.html'

    def get_success_url(self):
        return reverse('expense_success', args=[self.object.pk])

    def form_valid(self, form):
        form.instance.business_id = get_business_id(self.request)
        form.instance.created_by = self.request.user

        return super().form_valid(form)
    

# View all expenses
class ExpenseListView(ListView):
    model = Expense
    template_name = 'expense/expense_list.html'
    context_object_name = 'expenses'
    ordering = '-expense_date'

    def get_queryset(self):
        return Expense.objects.filter(
            business_id=get_business_id(self.request)
            ).select_related('category')

# View a particuler expense in detail
class ExpenseDetailView(DetailView):
    model = Expense
    context_object_name = 'expense'
    template_name = 'expense/expense_detail.html'

    def get_queryset(self):
        return Expense.objects.filter(business_id=get_business_id(self.request))
    
class ExpenseSuccessView(DetailView):
    model = Expense
    context_object_name = 'expense'
    template_name = 'expense/expense_success.html'

    def get_queryset(self):
        return Expense.objects.filter(business_id=get_business_id(self.request))

# Manage and create expense categories
class ExpenseCategoryView(CreateView):
    model = ExpenseCategory
    form_class = ExpenseCategoryForm
    template_name = 'expense/expense_categories.html'
    success_url = reverse_lazy('expense_categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ExpenseCategory.objects.filter(business_id=get_business_id(self.request)).order_by('-created_at')
        return context

    def form_valid(self, form):
        form.instance.business_id = get_business_id(self.request)

        return super().form_valid(form)
    


