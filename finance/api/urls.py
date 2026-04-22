from django.urls import path
from . import views

urlpatterns = [
    path('search-expenses/', views.ExpensesSearchView.as_view()),
    path('search-expense-categories/', views.ExpCategoriesSearchView.as_view()),
]
