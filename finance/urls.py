from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddExpenseView.as_view(), name='add_expense'),
    path('list/', views.ExpenseListView.as_view(), name='expense_list'),
    path('list/<int:pk>', views.ExpenseDetailView.as_view(), name='expense_detail'),
    path('categories/', views.ExpenseCategoryView.as_view(), name='expense_categories'),
    path('success/', views.AddExpenseView.as_view(), name='expense_success')
]
