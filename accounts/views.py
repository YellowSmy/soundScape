from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


from .models import Profile
from .forms import ProfileForm

## Base
def Profile_detail(request, user_id):
        profile = get_object_or_404(Profile, user_id=user_id)
        return render(request, "profile/profile.html", {'profile': profile})


# New
@login_required()
def Profile_new(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('accounts:profile', user_id=profile.user_id)
        
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile/profile_edit.html', {'form': form, 'submitText' : "생성"})

# Update
@login_required()
def Profile_modify(request, user_id):
    profile = get_object_or_404(Profile, user_id=user_id)

    if request.user == profile.user:
        #POST Request
        if request.method == "POST" and request.FILES.get('profile_img'):
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            
            if form.is_valid():
                profile = form.save(commit=False)
                profile.save()

                return redirect('accounts:profile', user_id=profile.user_id)
            
            else:
                return redirect('accounts:profile')
        
        #GET Request
        else:
            form = ProfileForm(instance=profile)
            return render(request, 'profile/profile_edit.html', {'form' : form, 'submitText' : "수정"}) 


## Follow
@login_required()
@require_POST
def Follow(request, user_id):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=user_id)

        if profile.user != request.user: #상대방 != 나 
            #unfollow
            if profile.followers.filter(user_id=request.user.profile.user_id).exists():
                profile.followers.remove(request.user.profile) 

            #follow
            else:
                profile.followers.add(request.user.profile)

        return redirect('accounts:profile', user_id)    
    
    return redirect('accounts:profile', user_id)