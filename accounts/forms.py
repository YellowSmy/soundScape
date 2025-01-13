from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Member

## 회원가입 Form 수정 (from allauth userCreationForm)
class SignupForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ['nickname']

    def signup(self, request, user):
        user.nickname = self.cleaned_data['nickname']
        user.save()
    