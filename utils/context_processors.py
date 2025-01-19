from accounts.models import Profile

def user_profile(request):
    if request.user.is_authenticated:
        try:
            profile = request.user.profile  
            return {'user_profile': profile}
        
        except Profile.DoesNotExist:
            return {'user_profile': None}  
        
    return {}