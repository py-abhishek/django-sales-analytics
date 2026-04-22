from django.urls import path
from . import views

urlpatterns = [
    path('search-customers/', views.CustomerSearchView.as_view()),
    path('search-sales/', views.SalesSearchView.as_view()),
]
