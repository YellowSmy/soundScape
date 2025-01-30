from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver

import os

from utils.file_upload import user_dir_path
from accounts.models import Member, Profile

@receiver(post_save, sender=Member)
def create_new_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(pre_save, sender=Profile)
def auto_delete_file_on_save(sender, instance, **kwargs):
        if not instance.pk:
             return False
        try:
             old_obj = sender.objects.get(pk=instance.pk)
        except sender.DoesNotExist:
             return False
        
        if old_obj.profile_img != instance.profile_img:
            if old_obj.profile_img and os.path.isfile(old_obj.profile_img.path):
                old_file_path = old_obj.profile_img.path
                new_file_path = user_dir_path(instance, instance.profile_img.name)  

                if old_file_path != new_file_path:
                    os.remove(old_file_path)