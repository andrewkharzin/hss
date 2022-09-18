from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        AIRLINE_AGENT = "AIRLINE_AGENT", "Airline_Agent"
        PROVISOR = "PROVISOR", "Provisor"

    base_role = Role.ADMIN



    role = models.CharField(max_length=50, choices=Role.choices)
   

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class AgentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.AIRLINE_AGENT)


class AirlineAgent(User):

    base_role = User.Role.ADMIN

    agent = AgentManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for airline agents"



class ProvisorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.PROVISOR)


class Provisor(User):

    base_role = User.Role.PROVISOR

    provisor = ProvisorManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for provisors"
