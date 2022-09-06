from django.contrib import admin
from apps.profiles.models import Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'agent',
    ]


admin.site.register(Profile, ProfileAdmin)
