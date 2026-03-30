from django.urls import path
from . import views

urlpatterns = [
    path('create', views.CreateBusinessView.as_view(), name='create_business'),
    path('select', views.SelectBusinessView.as_view(), name='select_business')
]
