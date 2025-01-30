import os, random
from django.conf import settings
from django.utils.crypto import get_random_string

from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from allauth.account.utils import perform_login

from accounts.models import Member, Profile

@require_POST
def Guest(request):
    username = get_random_string(length=5)
    email =  username + "@example.com"
    password = get_random_string(length=15)
       
    user = get_user_model().objects.create_user(
        username=username,
        email=email,        
        password=password,
        is_guest = True,
    )

    print(user.id)

    create_guest_profile(user.id)
    perform_login(request, user)
    
    return redirect('diary:index')


def create_guest_profile(user_id):
    profile = Profile.objects.get(user_id=user_id)

    file_path = os.path.join(settings.BASE_DIR, 'static', 'guest_nickname.txt')

    if not os.path.exists(file_path):
        print("NO FILE")

    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            lines = file.readlines()
            nickname = random.choice(lines).strip()
            profile.nickname = nickname
            profile.save()
            
        except Exception as e:
            print(e)