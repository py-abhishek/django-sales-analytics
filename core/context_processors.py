from business.models import Membership
from business.models import Business

# Access user_role globally
def user_role(request):
    if request.user.is_authenticated:
        business_id = request.session.get('business_id')

        if business_id:
            membership = Membership.objects.filter(
                business_id=business_id,
                user=request.user
            ).first()

            if membership:
                return {'user_role': membership.role}
    
    return {'user_role': None}


def current_business(request):
    if request.user.is_authenticated:
        business_id = request.session.get('business_id')

        current_business = Business.objects.filter(id=business_id).values_list('name', flat=True).first()

        return {'current_business': current_business}

    return {'current_business': None}