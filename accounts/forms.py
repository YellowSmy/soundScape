from django import forms
from django.forms import ImageField, FileInput,TextInput

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
    profile_img = ImageField(widget=FileInput, required=False)
    class Meta:
        model = Profile
        fields = ['nickname', 'profile_img', 'bio']

        widgets = {
            'nickname': TextInput(attrs={
                'placeholder': '닉네임..',
                'autocomplete' : 'off',
                'autofocus' : True,
                'spellcheck' : False,
            },),

            'bio': TextInput(attrs={
                'placeholder': '자기소개..',
                'autocomplete' : 'off',
                'spellcheck' : False,
            },)
        }

        labels = {
            'nickname' : "닉네임",
            'profile_img' : "프로필 이미지",
            'bio' : "자기소개..",
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.profile_img:
            self.fields['profile_img'].initial = self.instance.profile_img