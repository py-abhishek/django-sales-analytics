from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('signin', views.SignInView.as_view(), name='signin'),
    path('signout', views.sign_out, name='signout'),
    path('profile', views.UserProfileView.as_view(), name='profile'),
]
