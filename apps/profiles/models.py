from django.db import models
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from django.dispatch import receiver 
from django.db.models.signals import post_save 

class Profile(models.Model):   
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    agent = models.CharField(max_length=155, blank=True, null=True)

    
    @receiver(post_save, sender=settings.AUTH_USER_MODEL) #add this
    def create_user_profile(sender, instance, created, **kwargs):
            if created:
                Profile.objects.create(user=instance)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL) #add this
    def save_user_profile(sender, instance, **kwargs):
            instance.profile.save()
    

    

    def __str__(self):
        return f"{self.user.email}"
