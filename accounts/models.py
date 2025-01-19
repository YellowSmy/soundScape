from django.db import models
from django.contrib.auth.models import AbstractUser

## Authenticate Model
class Member(AbstractUser):

    def __str__(self):
        return self.email

## Profile
class Profile(models.Model):
    #Authenticate info.
    user = models.OneToOneField(Member, on_delete=models.CASCADE)

    # necessary
    nickname = models.CharField(max_length=20, unique=False)

    # unnecessary info.
    profile_img = models.ImageField(blank=True, upload_to='images/', default='images/default.png')
    bio = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nickname