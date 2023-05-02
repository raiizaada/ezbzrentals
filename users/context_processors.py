
from rentals.models import UserProfile

def add_user_profile(request):
    user = request.user
    profile_photo = None
    
    if user.is_authenticated:
        user_profile = UserProfile.objects.filter(user_id=user.id).first()
        if user_profile:
            profile_photo = user_profile.profile_photo
            if not profile_photo:
                first_name = user_profile.first_name
                last_name = user_profile.last_name
                if first_name and last_name:
                    profile_photo = f"{first_name[0].upper()}{last_name[0].upper()}"
    
    return {'profile_photo': profile_photo}

