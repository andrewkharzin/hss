from django.db import models
from apps.users.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from apps.agents.utils import unique_order_id_generator
from django.db.models.signals import pre_save
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Agent(models.Model):

    class Company(models.TextChoices):
        NW_TECHNIC = 'NW_TECH', _('Nord Avia Technics')
        AEROFLOT_DTO = 'AFL_TDO', _('Aeroflot Technics Directions')
        SKY_TECHNIK = 'SKY_TECH', _('Sky technik')
        UNSIGN = 'UNSiGN', _('UNSIGN')
    user = models.OneToOneField(User, verbose_name=_(
        "user_agent"), on_delete=models.CASCADE)
    agent_id = models.CharField(max_length=15, null=True, blank=True)
    agent_company = models.CharField(
        _("Agent company"), choices=Company.choices, max_length=50, null=True, default=Company.UNSIGN)
    phone_number = PhoneNumberField()
    phone_number_mobile = PhoneNumberField()

    def __str__(self):
        return f"{'AG_ID/'}{self.agent_id.upper()}-{self.agent_company}"


def pre_save_create_agent_id(sender, instance, *args, **kwargs):
    if not instance.agent_id:
        instance.agent_id = unique_order_id_generator(instance)


pre_save.connect(pre_save_create_agent_id, sender=Agent)


@receiver(post_save, sender=User)  # add this
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Agent.objects.create(user=instance)


@receiver(post_save, sender=User)  # add this
def save_user_profile(sender, instance, **kwargs):
    instance.agent.save()
