from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm, SignInForm


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

            return redirect(reverse_lazy('create_business'))
        
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
            return redirect(reverse_lazy('dashboard'))
            
        errors.append('Email or password is incorrect')
        
        return render(request, 'accounts/sign_in.html', {'errors': errors})