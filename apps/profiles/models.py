from django.db import models
from apps.users.models import Provisor, AirlineAgent
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from apps.profiles.uuid import BaseUUID
from django.urls import reverse
from pytils.translit import slugify
from apps.organizations.models import Organization


class Profile(models.Model):
    # class Meta:
    #     abstract = True

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(
        _("Phone number"), max_length=12, null=True, blank=True
    )
    position = models.CharField(_("Position"), max_length=75, default="")
    # company = models.OneToOneField(
    #     Organization, related_name="user_organization", on_delete=models.CASCADE
    # )
    user_image = models.ImageField(
        _("User Image"),
        upload_to="uploads/users/profiles/%Y/%m/%d/",
        null=True,
        blank=True, default='uploads/users/profiles/default.png'
    )
    slug = models.SlugField(null=True, blank=True)
    full_name = models.CharField( max_length=255)
   
    
    def get_absolute_url(self, *args, **kw ):
      return reverse('profile_settings', kwargs={'pk': self.pk})
  
    def save(self, *args, **kwargs): # new
       
        if not self.slug:
            self.slug = slugify(self.phone_number)
        return super( Profile, self).save(*args, **kwargs)


    @property
    def thumbnail_preview(self):
        if self.user_image:
            _user_image = get_thumbnail(
                self.user_image, "80", upscale=False, crop=False, quality=100
            )
            return format_html(
                '<img src="{}" width="{}" height="{}">'.format(
                    _user_image.url, _user_image.width, _user_image.height
                )
            )
        return ""

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)  # add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)  # add this
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f"{self.user}"

    def get_profile_fields(self):
        return f"{self.first_name}-{self.last_name}-{self.phone_number}{self.position}"

    # def save(self, *args, **kwargs):
    #     qrcode_img = qrcode.make(self.get_profile_fields)
    #     canvas = Image.new('RGB', (290, 290), 'white')
    #     draw = ImageDraw.Draw(canvas)
    #     canvas.paste(qrcode_img)
    #     fname = f'qr_code-{self.get_profile_fields}'+'.png'
    #     buffer = BytesIO()
    #     canvas.save(buffer, 'PNG')
    #     self.qr_code.save(fname, File(buffer), save=False)
    #     canvas.close()
    #     super().save(*args, **kwargs)


# Airline agent profile
class AirlineAgentProfile(models.Model):
    airline_agent_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=AirlineAgent)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "AIRLINE_AGENT":
        AirlineAgentProfile.objects.create(user=instance)


# Provisor profile
class ProvisorProfile(Profile):
    provisor_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=Provisor)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "PROVISOR":
        ProvisorProfile.objects.create(user=instance)
        
        
class UserFullName(Profile):
    class Meta: 
        proxy = True 
    def __unicode__(self): 
        return self.get_full_name()
