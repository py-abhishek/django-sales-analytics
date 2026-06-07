
from django.shortcuts import redirect
from .utils import has_role
from django.contrib import messages

class RoleRequiredMixin:
    allowed_roles = []

    def dispatch(self, request, *args, **kwargs):
        business_id = request.session.get('business_id')

        if not has_role(request.user, business_id, self.allowed_roles):
            messages.error(
                request,
                "You don't have permission to perform this action."
            )
            
            if self.permission_denied_url:
                return redirect(self.permission_denied_url, pk=kwargs.get('pk'))

            return redirect('dashboard')
        
        return super().dispatch(request, *args, **kwargs)