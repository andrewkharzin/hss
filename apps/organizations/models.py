from django.db import models
from django.conf import settings
from apps.users.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from apps.organizations.uuid import BaseUUID


class Organization(BaseUUID):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    organization_name = models.CharField(
        _("Company Name"), max_length=50, default="Person Company LTD")
    address = models.TextField()
    ogrn_number = models.CharField(_("ОГРН"), max_length=13)
    inn_number = models.CharField(_("ИНН"), max_length=10)
    kpp_number = models.CharField(_("КПП"), max_length=9)
    website = models.URLField(_("Web Site Url"), max_length=200)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)  # add this
    def create_user_company(sender, instance, created, **kwargs):
        if created:
            Organization.objects.create(user=instance)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)  # add this
    def save_user_compnay(sender, instance, **kwargs):
        instance.organization.save()

    def __str__(self):
        return f"{self.user}  -  {self.organization_name}"
