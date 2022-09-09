from django.contrib import admin
from apps.stuffs.models import Aog, AcEngine


class AogAdmin(admin.ModelAdmin):
    pass


class AcEngineAdmin(admin.ModelAdmin):
    pass


admin.site.register(Aog, AogAdmin)
admin.site.register(AcEngine, AcEngineAdmin)
