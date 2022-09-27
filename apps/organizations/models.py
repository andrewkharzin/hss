from django.db import models
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html
from django.conf import settings
from apps.users.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from apps.organizations.uuid import BaseUUID
from urllib.parse import urlparse


class Organization(BaseUUID):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization_name = models.CharField(
        _("Company Name"), max_length=50, default="Person Company LTD"
    )
    address = models.TextField()
    country = models.CharField(_("Country"), max_length=65, default="")
    ogrn_number = models.CharField(_("ОГРН"), max_length=13)
    inn_number = models.CharField(_("ИНН"), max_length=10)
    kpp_number = models.CharField(_("КПП"), max_length=9)
    website = models.URLField(_("Web Site Url"), max_length=200)
    org_icon = models.ImageField(
        _("User Image"),
        upload_to="uploads/users/organizations/%Y/%m/%d/",
        null=True,
        blank=True,
    )
    
    def url_text(self):
        parsed_url = urlparse(self.website)
        return parsed_url.hostname.replace("http://.", "www.") + ""

    @property
    def thumbnail_preview(self):
        if self.org_icon:
            _org_icon = get_thumbnail(
                self.org_icon, "35", upscale=False, crop=False, quality=100
            )
            return format_html(
                '<img src="{}" width="{}" height="{}">'.format(
                    _org_icon.url, _org_icon.width, _org_icon.height
                )
            )
        return ""

    # def getImage(self):
    #     if user.Role

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)  # add this
    def create_user_company(sender, instance, created, **kwargs):
        if created:
            Organization.objects.create(user=instance)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)  # add this
    def save_user_compnay(sender, instance, **kwargs):
        instance.organization.save()

    def __str__(self):
        return f"{self.user}  -  {self.organization_name}"
