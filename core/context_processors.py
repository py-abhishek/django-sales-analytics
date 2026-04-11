from business.models import Membership

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