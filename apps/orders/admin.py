from django.contrib import admin

from apps.orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        # 'order_agent',
        'service',
        'order_createAt',
        'order_updateAt',
        'order_status',

    ]

    list_display_links = [
        'service',
    ]
# Register your models here.


admin.site.register(Order, OrderAdmin)
