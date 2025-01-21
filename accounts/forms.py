from django import forms
from django.forms import ImageField, FileInput

from django.contrib.auth.forms import UserCreationForm

from .models import Member, Profile

## 회원가입 Form 수정 (from allauth userCreationForm)
class SignupForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ['email', 'password1', 'password2']

    def signup(self, request, user):
        user.save()


## Profile Form
class ProfileForm(forms.ModelForm):
    profile_img = ImageField(widget=FileInput)
    class Meta:
        model = Profile
        fields = ['nickname', 'profile_img', 'bio']

        labels = {
            'nickname' : "닉네임",
            'profile_img' : "프로필 이미지",
            'bio' : "자기소개..",
        }
    