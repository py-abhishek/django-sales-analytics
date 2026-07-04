from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView

from . import services
from business.models import Membership
from core.permissions.mixins import RoleRequiredMixin

# Create your views here.

# Manage particular business users
class ManageUsersView(RoleRequiredMixin, View):
    allowed_roles = [Membership.UserRoleChoices.OWNER, Membership.UserRoleChoices.ADMIN]

    def get(self, request):
        bussiness_members = Membership.objects.filter(business_id=request.session.get('business_id')).order_by('user__first_name')

        return render(request, 'users/manage_users.html', {'business_members':bussiness_members})
    
    def post(self, request):
        context = {}
        form_type = request.POST.get('form_type')

        # Add new user
        if form_type == 'add_user':
            context = services.add_user(request)
        
        # Edit user role
        elif form_type == 'edit_role':
            context['edit_form'] = services.edit_role(request)

        # Delete user
        elif form_type == 'delete_user':
            context['delete_form'] = services.delete_user(request)

        bussiness_members = Membership.objects.filter(business_id=request.session.get('business_id')).order_by('user__first_name')

        context['business_members'] = bussiness_members
        # print(context)

        return render(request, 'users/manage_users.html', context)
    
