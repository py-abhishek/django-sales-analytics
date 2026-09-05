
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# check if password is strong enough
def check_password(password:str):
    if len(password) < 8:
        return False
    
    has_letter = any(char.isalpha() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_special = any(char.isalnum() for char in password)
    has_upper = any(char.isupper() for char in password)

    return has_letter and has_number and has_special and has_upper

# update user profile
def update_profile(request):
    context = {}
    first_name = request.POST.get('first_name')
    if not first_name:
        context['form1_error'] = 'First name is required'
    
    else:
        request.user.first_name = first_name
        request.user.last_name = request.POST.get('last_name')
        request.user.save()
        context['form1_info'] = 'Profile updated successfully'
        messages.success(request, context.get('form1_info'))
    
    return context

# update user password
def update_password(request):
    context = {}
    c_pass = request.POST.get('current_password')
    new_pass = request.POST.get('new_password')
    confirm_pass = request.POST.get('confirm_password')

    if not c_pass:
        context['form2_error'] = 'Please enter current password'

    elif not request.user.check_password(c_pass):
        context['form2_error'] = 'Current password is incorrect'
    
    elif not new_pass:
        context['form2_error'] = 'Please enter a new password'

    if not check_password():
        context['form2_error'] = 'Password must be at least 8 characters and include uppercase, lowercase, number, and special character.'
        
    elif not new_pass == confirm_pass:
        context['form2_error'] = 'Passwords do not match'
    
    else:
        request.user.set_password(new_pass)
        request.user.save()
        update_session_auth_hash(request, request.user)
        context['form2_info'] = 'Password changed successfully'
        messages.success(request, context.get('form2_info'))
    
    return context