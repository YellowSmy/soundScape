from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Member, Profile

@receiver(post_save, sender=Member)
def create_new_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)