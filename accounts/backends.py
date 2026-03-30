from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

'''
Custom authentication backend is required because we are using email
instead of username, but django still requires username for authentication.
So we can use django's default authenticate() function.

'''

User = get_user_model()

class EmailBackend(ModelBackend):

    def authenticate(self, request, username = None, password = None, **kwargs):
        
        email = username  # Django still passes username

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        
        return None
        
