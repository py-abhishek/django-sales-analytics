from django.shortcuts import redirect

# No access without login
class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        if request.path.startswith('/accounts/'):
            return self.get_response(request)
        
        if not request.user.is_authenticated:
            return redirect('signin')
        
        return self.get_response(request)
    

# Block access if no business is selected
class BusinessRequiredMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        # Skip for auth pages
        if request.path.startswith('/accounts/'):
            return self.get_response(request)
        
         # Skip for create/select business pages
        if request.path.startswith('/business/'):
            return self.get_response(request)
        
        # Check if business is selected
        if request.user.is_authenticated:
            business_id = request.session.get('business_id')

            if not business_id:
                return redirect('select_business')
            
        return self.get_response(request)