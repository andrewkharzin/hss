from django.contrib import admin
from apps.users.models import User

admin.site.register(User)


# class UserAdminConfig(UserAdmin):
#     model = User
#     search_fields = ('email',)
#     # list_filter = ('email', 'is_active', 'is_staff')
#     list_display = ('email',
#                     'is_active', 'is_staff')
#     fieldsets = (
#         (None, {'fields': ('email',)}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),

#     )
#     formfield_overrides = {
#         models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
#     }
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff')}
#          ),
#     )


# admin.site.register(User, UserAdminConfig)
