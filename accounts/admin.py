from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Member, Profile

# Register your models here.
admin.site.register(Member)
admin.site.register(Profile)
UserAdmin.fieldsets += (("Custom fields", {"fields":("nickname", )}),)
