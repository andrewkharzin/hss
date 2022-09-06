from django.db import models
from django.db.models.signals import post_save
from apps.ssr.models import Request
from django.utils.translation import gettext_lazy as _
import uuid


class CustomDateTimeField(models.DateTimeField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return ''


class Order(models.Model):

    class OrderStatus(models.TextChoices):
        ACCEPT = 'ACP', _('Order accepted')
        CONFIRMED = 'CNF', _('Order confirmed')
        COMPLETED = 'CPD', _('Order completed')
        REJECTED = 'RJD', _('Order rejected')

    request = models.OneToOneField(Request, on_delete=models.CASCADE)
    order_number = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    # order_agent = models.ForeignKey(
    #     Agent, related_name='agent_orders', on_delete=models.CASCADE, null=True)
    order_createAt = CustomDateTimeField(auto_now=True)
    order_updateAt = CustomDateTimeField(auto_now_add=True)
    order_status = models.CharField(
        max_length=50, choices=OrderStatus.choices, default=OrderStatus.ACCEPT)

    # def __str__(self):
    #     return f"{self.order_number}/{self.order_agent}/{self.request}/{self.order_createAt}/{self.order_updateAt}/{self.order_status}"

    def __str__(self):
        return str(self.request)


def create_order(sender, instance, created, **kwargs):

    if created:
        Order.objects.create(request=instance)
        print('Order Created')


post_save.connect(create_order, sender=Request)


def update_order(sender, instance, created, **kwargs):
    if created == False:
        instance.order.save
        print('Order Updated')


post_save.connect(update_order, sender=Request)
