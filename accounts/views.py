from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm
from business.models import Membership, Business
from . import services


# Create your views here.
class SignUpView(View):
    def get(self, request):
        form = SignUpForm()

        context = {
            'form': form
        }
        return render(request, 'accounts/sign_up.html', context)
    
    def post(self, request):
        form = SignUpForm(request.POST)
        password1 = request.POST.get('password1').strip()
        password2 = request.POST.get('password2').strip()

        if password1 != password2:
            form.add_error(None, "Password do not match")

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(password1)
            user.save()

            login(request, user)

            return redirect('create_business')
        
        else:
            return render(request, 'accounts/sign_up.html', {'form': form})
        
        

class SignInView(View):
    def get(self, request):
        return render(request, 'accounts/sign_in.html')
    
    def post(self, request):
        errors = []
        email = request.POST.get('email').strip()
        password = request.POST.get('password').strip() 

        user = authenticate(request, username=email, password= password)
        
        if user is not None:
            login(request, user)

            membership = Membership.objects.filter(user=user)

            # Only one business exists
            if len(membership) == 1:
                request.session['business_id'] = membership[0].business.id
                return redirect('dashboard')
            
            # Multiple or No Businesses exists
            else:
                return redirect('select_business')
            
        errors.append('Email or password is incorrect')
        
        return render(request, 'accounts/sign_in.html', {'errors': errors})
    

def sign_out(request):
    logout(request)
    return redirect('signin')


# User Profile
class UserProfileView(View):
    def get(self, request):
        business_id = request.session.get('business_id')
        memberships = Membership.objects.filter(user=request.user)
        current_business = Business.objects.get(id=business_id)

        context = {
            'memberships': memberships,
            'current_business': current_business
        }

        return render(request, 'accounts/user_profile.html', context)
    

    def post(self, request):
        # Update profile
        if 'update_profile' in request.POST:
            context = services.update_profile(request)
        
        # Update password
        elif 'update_password' in request.POST:
            context = services.update_password(request)
            

        return render(request, 'accounts/user_profile.html', context)