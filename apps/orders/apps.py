from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class OrdersConfig(AppConfig):
    name = 'apps.orders'
    verbose_name = _('orders')
