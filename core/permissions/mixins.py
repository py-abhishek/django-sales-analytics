from django.http import HttpResponseForbidden
from .utils import has_role

class RoleRequiredMixin:
    allowed_roles = []

    def dispatch(self, request, *args, **kwargs):
        business_id = request.session.get('business_id')

        if not has_role(request.user, business_id, self.allowed_roles):
            return HttpResponseForbidden('Permission denied')
        
        return super().dispatch(request, *args, **kwargs)