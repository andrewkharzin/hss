from django.contrib import admin
from apps.users.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea
from django.db import models


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'username', )
    list_filter = ('email', 'username', 'is_active', 'is_staff')
    list_display = ('email', 'username',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username', )}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(User, UserAdminConfig)