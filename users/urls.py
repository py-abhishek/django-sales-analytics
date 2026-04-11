from django.urls import path
from . import views

urlpatterns = [
    path('', views.ManageUsersView.as_view(), name='manage_users')
]
