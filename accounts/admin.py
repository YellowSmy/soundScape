from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Member

# Register your models here.
admin.site.register(Member)
UserAdmin.fieldsets += (("Custom fields", {"fields":("nickname", )}),)