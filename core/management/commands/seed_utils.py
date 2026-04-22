from django.db import transaction
from accounts.models import User
from business.models import Business, Membership

def get_or_create_membership():
    # Email: abhishek@test.com | Password: 1198
    # Check if user exits
    email = 'abhishek@test.com'
    user = User.objects.filter(email=email).first()

    if not user:
        # Create new user
        user = User(
            first_name='Abhishek',
            last_name='Chaudhary',
            email=email,
        )
        user.set_password('1198')
        user.save()
    
    # Create business and membership
    return create_business(user)



def create_business(user):
    business_name = 'Riam Electronics'
    business = Business.objects.filter(name=business_name).first()
    membership = Membership.objects.filter(user=user, business=business).first()

    if not business:
        with transaction.atomic():
            business = Business(
                name='Riam Electronics',
                business_type=Business.BusinessTypeChoices.RETAIL,
                phone='',
                email='',
                address='',
                created_by=user
            )
            business.save()

            membership = Membership.objects.create(
                user=user,
                business=business,
                role=Membership.UserRoleChoices.ADMIN
            )

    return membership
