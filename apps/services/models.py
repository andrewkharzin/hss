from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.services.uuid import BaseUUID
from apps.agents.models import Agent
from apps.stuffs.models import Aog


class BaseServiceRequest(BaseUUID):
    data_createAt = models.DateTimeField(
        _("DateTime created"), auto_now=True, editable=False)
    data_updateAt = models.DateTimeField(
        _("DateTime updated"), auto_now=False, auto_now_add=True, editable=False)

    agent = name = models.ForeignKey(
        Agent, related_name='agent_service_request', on_delete=models.CASCADE)
    service_date = models.DateField(
        _("Service date"), auto_now=False, auto_now_add=False)
    service_time = models.TimeField(
        _("Service time"), auto_now=False, auto_now_add=False)

    class Meta:
        abstract = True


class AogService(BaseServiceRequest):

    aog_type = (
        ("loading", "Loading"),
        ("offloading", "Offloading"),
    )
    # service_item = models.ManyToManyField(
    #     Aog, related_name="aog_service_items")
    service_name = models.CharField(
        _("Service name"), max_length=50, blank=False, null=False)
    aog_type = models.CharField(_("Type"), max_length=50, choices=aog_type)
    flight = models.CharField(_("Flight"), max_length=7)
    flight_ac_reg = models.CharField(
        _("AC Registration"), max_length=8, default='')
    flight_date = models.DateField(
        _("Flight date"), auto_now=False, auto_now_add=False, null=True, blank=True)
    flight_time = models.TimeField(
        _("Flight time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    aog_item = models.ManyToManyField(Aog)
    description = models.TextField()


    def __str__(self):
        return f" {self.service_name} / {self.service_date} / {self.aog_type.upper()} | {self.flight.upper()} | {self.agent}"
