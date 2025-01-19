from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Profile
from .forms import ProfileForm

# Create
def Profile_detail(request, user_id):
        profile = get_object_or_404(Profile, user_id=user_id)
        return render(request, "account/profile.html", {'profile': profile})


# Update
@login_required()
def Profile_modify(request, user_id):
    profile = get_object_or_404(Profile, user_id=user_id)

    if request.user == profile.user:
        #POST Request
        if request.method == "POST":
            form = ProfileForm(request.POST, instance=profile)
            
            if form.is_valid():
                profile = form.save(commit=False)
                profile.save()
                return redirect('accounts:profile', user_id=profile.user_id)
            
            else:
                return redirect('accounts:profile')
        
        #GET Request
        else:
            form = ProfileForm(instance=profile)
            return render(request, 'account/editProfile.html', {'form' : form }) 


