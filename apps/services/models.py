from django.db import models
from apps.agents.models import Agent
from django.utils.translation import gettext_lazy as _
from apps.services.uuid import BaseUUID
from apps.agents.models import Agent
from apps.stuffs.models import Aog
from django.shortcuts import reverse
# from django.http import HttpResponseRedirect
# from django.http import FileResponse
# import io
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter

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
    agent = models.ForeignKey(
        Agent, related_name='agent_services_request', on_delete=models.CASCADE)
    aog_type = (
        ("loading", "Loading Wheels"),
        ("offloading", "Unloading Wheels"),
    )
    # service_item = models.ManyToManyField(
    #     Aog, related_name="aog_service_items")
   
    service_name = models.CharField(_("Service Name"), max_length=50, choices=aog_type)
    flight = models.CharField(_("Flight"), max_length=7)
    flight_ac_reg = models.CharField(
        _("AC Registration"), max_length=8, default='')
    flight_date = models.DateField(
        _("Flight date"), auto_now=False, auto_now_add=False, null=True, blank=True)
    flight_time = models.TimeField(
        _("Flight time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    aog_item = models.ManyToManyField(Aog)
    fix_required = models.BooleanField(default=False)
    starps_count = models.IntegerField(null=True, blank=True)
    responsibles_persons = models.ManyToManyField(
        'DutyPerson')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.service_name}"
    def __str__(self):
        return self.get_service_name_display()

    def get_name(request):
        return responsibles_persons.full_name

    def get_absolute_url(self):
        return reverse("AogService", kwargs={"pk": self.pk})



    


class DutyPerson(BaseUUID):
    full_name = models.CharField(_("Full Name"), max_length=50)
    position = models.CharField(_("Person position"), max_length=50)
    contact_phone = models.CharField(_("Contact Phone"), max_length=12)

    def __str__(self):
        return self.full_name
