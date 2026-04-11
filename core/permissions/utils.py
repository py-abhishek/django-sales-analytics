from business.models import Membership, Business

# Returns role of user in specific business
def get_user_role(user, business_id):
    if not user.is_authenticated:
        return None
    
    membership = Membership.objects.filter(user=user, business_id=business_id).first()
    return membership.role if membership else None
    

# Check if current user has any allowed role
def has_role(user, business_id, allowed_roles):
    role = get_user_role(user, business_id)
    return role in allowed_roles