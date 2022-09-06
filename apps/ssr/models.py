from django.db import models
from apps.agents.models import Agent

from django.utils.translation import gettext_lazy as _


class Request(models.Model):

    class OrderType(models.TextChoices):
        AOG_SERVICE = 'AOG', _('Aog service')
        BALLAST_HND = 'BLS', _('Ballast handling')
        TRANSPORT_SRV = 'TRA', _('Transport, loading service')
        NEW = 'NEW', _('New request')

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="send_request")

    options = (
        ("draft", "Draft"),
        ("send", "Send"),
    )
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    order_number = models.AutoField(primary_key=True)
    service_type = models.CharField(
        max_length=3, choices=OrderType.choices, default=OrderType.NEW)
    title = models.CharField(max_length=155, blank=False, null=False)

    body = models.TextField()
    service_date = models.DateTimeField(blank=True)

    request_status = models.CharField(
        max_length=10, choices=options, default="draft")
    creatAt = models.DateTimeField(auto_now=True)
    updateAt = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    class Meta:
        ordering = ("-service_date",)

    # def save(self, *args, **kwargs):
    #     if not self.order_number:
    #         self.order = f"{F('order_number') + F('service_type') + 1}"

    #         return super(ServiceOrderRequest, self).save(*args, **kwargs)

    def __str__(self):
        return f"{'FROM'}  //  {self.agent}->{self.order_number}| {'SERVICE'} // {self.service_type}/{self.creatAt.strftime('%m/%d/%Y %H:%M')}"
