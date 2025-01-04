from django.db import models
from django.contrib.auth.models import AbstractUser

## Users
class Member(AbstractUser):
    # Django Users use

    # +email 인증 관련
    email_vertified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=255, blank=True, null=True)
    
    # 사용자 정보

