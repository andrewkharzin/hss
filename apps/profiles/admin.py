from django.contrib import admin
from apps.profiles.models import Profile, AirlineAgentProfile, ProvisorProfile


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'first_name',
        'last_name',
        'position',
        
    ]



admin.site.register(Profile, ProfileAdmin)
admin.site.register(AirlineAgentProfile)
admin.site.register(ProvisorProfile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = [
#         'user',
#         'first_name',
#         'last_name',
#         'phone_number',
#         'email',
#         'position',
#         'thumbnail_preview',

#     ]

#     readonly_fields = ('thumbnail_preview',)

#     def thumbnail_preview(self, obj):
#         return obj.thumbnail_preview

#     thumbnail_preview.short_description = 'Thumbnail Preview'
#     thumbnail_preview.allow_tags = True


# admin.site.register(Profile, ProfileAdmin)
