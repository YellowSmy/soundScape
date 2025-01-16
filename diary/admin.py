from django.contrib import admin

from .models import Diary, Comment

# Register your models here.
admin.site.register(Diary)
admin.site.register(Comment)