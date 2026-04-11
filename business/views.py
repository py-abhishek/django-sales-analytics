from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from .forms import BusinessForm
from .models import Membership
from .services import create_business

# Create your views here.

# Create new business
class CreateBusinessView(View):
    def get(self, request):
        form = BusinessForm()
        return render(request, 'business/create_business.html', {'form': form})
    
    def post(self, request):
        business_form = BusinessForm(request.POST)
        user = request.user # Get current signed in user

        if business_form.is_valid():
            created_business = create_business(business_form, user)
            request.session['business_id'] = created_business.id # Saving buiness_id in session
            return redirect('dashboard')
        
        return render(request, 'business/create_business.html', {'form': business_form})


# Select from existing business
class SelectBusinessView(View):
    def get(self, request):
        user = request.user

        memberships  = Membership.objects.filter(user=user)

        print(memberships)
        
        return render(request, 'business/select_business.html', {'memberships': memberships})
    

# store active business id in session
def set_active_business(request, business_id):
    membership = get_object_or_404(
        Membership,
        user=request.user,
        business_id=business_id,
        is_active=True
        )
    
    request.session['business_id'] = membership.business.id

    return redirect('dashboard')