from django.db import models
from django.contrib.auth.models import AbstractUser

## Users
class Member(AbstractUser):
    nickname = models.CharField(max_length=20, unique=False)

    def __str__(self):
        return self.email
