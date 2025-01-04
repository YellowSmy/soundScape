from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Member

## 회원가입 Form 생성
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="email")

    class Meta:
        model = Member
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        
        """
        이메일 인증
        #user.email_vertified = False
        #user.email_token = self.generate_email_token()
        """

        if commit:
            user.save()

        return user

    """
    def generate_email_token(self):
        import uuid
        return str(uuid.uuid4())
    """