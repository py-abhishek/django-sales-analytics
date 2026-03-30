from django.shortcuts import render
from django.views.generic import View

# Create your views here.

# Create new business
class CreateBusinessView(View):
    def get(self, request):
        return render(request, 'business/create_business.html')


# Select from existing business
class SelectBusinessView(View):
    def get(self, request):
        return render(request, 'business/select_business.html')