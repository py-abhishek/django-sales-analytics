from accounts.models import User
from business.models import Membership, Business
from django.db import transaction, IntegrityError


def add_user(request):
    context = {}
    user_form = {}

    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    role = request.POST.get('role')

    if not first_name:
        user_form['error'] = 'First name is required'

    elif not email:
        user_form['error'] = 'Email is required'
    
    elif not password1:
        user_form['error'] = 'Password is required'

    elif not password1 == password2:
        user_form['error'] = 'Passwords do not match'
        
    else:
        business = Business.objects.get(id=request.session.get('business_id'))
        user_exits = False
        # Check if user already exits
        try:
            user = User.objects.get(email=email)
            user_exits = True
        except User.DoesNotExist:
            user = None
            user_exits = False

        # Validate role
        if role == 'admin':
            user_role = Membership.UserRoleChoices.ADMIN
        
        elif role == 'staff':
            user_role = Membership.UserRoleChoices.STAFF
        
        else:
            user_form['error'] = 'Undefined role'

        with transaction.atomic():
            if not user_exits:
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
            except IntegrityError:
                user_form['error'] = 'User already exits in this business'

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
    
    user = User.objects.get(id=user_id)
    business = Business.objects.get(id=request.session.get('business_id'))
    membership = Membership.objects.get(user=user, business=business)

    if role == 'admin':
        user_role = Membership.UserRoleChoices.ADMIN
    elif role == 'staff':
        user_role = Membership.UserRoleChoices.STAFF

    all_memberships = Membership.objects.filter(business=business, role=Membership.UserRoleChoices.ADMIN)
    if len(all_memberships) == 1 and membership.role == Membership.UserRoleChoices.ADMIN:
        edit_form['error'] = 'Role can not be changed. One admin is required to manage the business'

    else:
        membership.role = user_role
        membership.save()
        edit_form['info'] = 'User role changed successfully'
    
    # if error occures
    if edit_form['error']:
        edit_form['data'] = {}
        edit_form['data']['user_id'] = user_id
        edit_form['data']['name'] = request.POST.get('name')
        edit_form['data']['role'] = role

    return edit_form
    

# Delete user
def delete_user(request):
    delete_form = {}
    user_id = request.POST.get('user_id')
    user = User.objects.get(id=user_id)
    business = Business.objects.get(id=request.session.get('business_id'))
    membership = Membership.objects.get(user=user, business=business)

    all_memberships = Membership.objects.filter(business=business, role=Membership.UserRoleChoices.ADMIN)
    print(len(all_memberships))
    if len(all_memberships) == 1 and membership.role == Membership.UserRoleChoices.ADMIN:
        delete_form['error'] = 'User can not be deleted. One admin is required to manage the business'
        
    else:
        membership.delete()
        delete_form['info'] = 'User deleted successfully'
    
        # if error occures
    if delete_form['error']:
        delete_form['data'] = {}
        delete_form['data']['user_id'] = user_id
        delete_form['data']['name'] = request.POST.get('name')
    
    return delete_form
