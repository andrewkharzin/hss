from django.contrib import admin
from apps.stuffs.models import Aog, AcEngine
from simple_history.admin import SimpleHistoryAdmin


class AogAdmin(admin.ModelAdmin):
    list_display = [
        'item',
        'item_weight',
        'item_part_number',
        'item_history',
    ]


class AcEngineAdmin(admin.ModelAdmin):
    pass


admin.site.register(Aog, AogAdmin)
admin.site.register(AcEngine, AcEngineAdmin)
