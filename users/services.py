from accounts.models import User
from business.models import Membership, Business
from django.db import transaction, IntegrityError
from django.contrib import messages

# Validate and add new user
def add_user(request):
    context = {}
    user_form = {}

    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    role = request.POST.get('role')

    # Check if user already exits
    if not email:
        user_form['error'] = 'Email is required'

    user_exits = False
    user = None
    valid_user = True
    try:
        user = User.objects.get(email=email)
        user_exits = True
    except User.DoesNotExist:
        user = None
        user_exits = False

    ##############

    if not user_exits:
        if not first_name:
            user_form['error'] = 'New user, first name is required'
            valid_user = False

        elif not email:
            user_form['error'] = 'Email is required'
            valid_user = False
        
        elif not password1:
            user_form['error'] = 'Password is required'
            valid_user = False

        elif not password1 == password2:
            user_form['error'] = 'Passwords do not match'
            valid_user = False
            
    # Get current business id
    business = Business.objects.get(id=request.session.get('business_id'))

    # Validate role
    
    if role == 'owner':
        user_role = Membership.UserRoleChoices.OWNER

    elif role == 'admin':
        user_role = Membership.UserRoleChoices.ADMIN
    
    elif role == 'staff':
        user_role = Membership.UserRoleChoices.STAFF
    
    else:
        user_form['error'] = 'Undefined role'

    with transaction.atomic():
        if not user_exits and valid_user:
            user = User(
                first_name=first_name,
                last_name=last_name,
                email=email
            )

            user.set_password(password1)
            user.save()

        try:
            context['membership'] = Membership.objects.create(
                user=user,
                business=business,
                role=user_role
            )
            user_form['info'] = 'User added successfully'
            messages.success(request, user_form.get('info'))

        except IntegrityError:
            if valid_user:
                user_form['info'] = 'User already exits in this business'
                messages.info(request, user_form.get('info'))


    # Resending fields data in case of any error
    if user_form.get('error'):
        user_form['data'] = {}
        user_form['data']['first_name'] = first_name
        user_form['data']['last_name'] = last_name
        user_form['data']['email'] = email
        user_form['data']['role'] = role
    
    context['user_form'] = user_form

    return context

    
# Edit existing user role
def edit_role(request):
    edit_form = {}
    user_id = request.POST.get('user_id')
    role = request.POST.get('role')
    name = request.POST.get('name')
    
    user = User.objects.get(id=user_id)
    business = Business.objects.get(id=request.session.get('business_id'))
    membership = Membership.objects.get(user=user, business=business)

    if role == 'owner':
        user_role = Membership.UserRoleChoices.OWNER
    elif role == 'admin':
        user_role = Membership.UserRoleChoices.ADMIN
    elif role == 'staff':
        user_role = Membership.UserRoleChoices.STAFF

    all_memberships = Membership.objects.filter(business=business, role=Membership.UserRoleChoices.OWNER)
    if len(all_memberships) == 1 and membership.role == Membership.UserRoleChoices.OWNER:
        edit_form['error'] = 'Role can not be changed. One owner is required to manage the business'

    else:
        membership.role = user_role
        membership.save()
        edit_form['info'] = 'User role changed successfully'
        messages.success(request, edit_form.get('info'))
    
    # if error occures
    if edit_form.get('error'):
        edit_form['data'] = {}
        edit_form['data']['user_id'] = user_id
        edit_form['data']['role'] = role
        edit_form['data']['name'] = name

    return edit_form
    

# Delete user
def delete_user(request):
    delete_form = {}
    user_id = request.POST.get('user_id')
    user = User.objects.get(id=user_id)
    name = request.POST.get('name')

    business = Business.objects.get(id=request.session.get('business_id'))
    membership = Membership.objects.get(user=user, business=business)

    all_memberships = Membership.objects.filter(business=business, role=Membership.UserRoleChoices.OWNER)
    print(len(all_memberships))
    if len(all_memberships) == 1 and membership.role == Membership.UserRoleChoices.OWNER:
        delete_form['error'] = 'User can not be deleted. One owner is required to manage the business'
        
    else:
        membership.delete()
        delete_form['info'] = 'User deleted successfully'
        messages.success(request, delete_form.get('info'))
    
        # if error occures
    if delete_form.get('error'):
        delete_form['data'] = {}
        delete_form['data']['user_id'] = user_id
        delete_form['data']['name'] = name
    
    return delete_form
