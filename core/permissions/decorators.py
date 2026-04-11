from django.http import HttpResponseForbidden
from functools import wraps
from .utils import has_role


def role_required(allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            business_id = request.session.get('business_id')

            if not has_role(request.user, business_id, allowed_roles):
                return HttpResponseForbidden('Permission denied')
            
            return func(request, *args, **kwargs)
        
        return wrapper
    return decorator


def admin_required(func):
    return role_required(['admin'])(func)
