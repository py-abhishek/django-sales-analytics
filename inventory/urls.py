from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddProductView.as_view()),
    path('success/', views.AddProductView.as_view())
]