from django.db import transaction
from .models import Membership

def create_business(business_form, user):

    with transaction.atomic():
        business = business_form.save(commit=False)
        business.created_by = user
        business.save()

        Membership.objects.create(
            user=user,
            business=business,
            role=Membership.UserRoleChoices.ADMIN
        )

        return business
