from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MetroUser


@admin.register(MetroUser)
class MetroUserAdmin(UserAdmin):
    """Администратор пользователей."""

    list_display = (
        'email',
        'full_name',
    )

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'full_name', 'avatar', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'full_name', 'avatar', 'address'),
        }),
    )

    search_fields = (
        'email',
        'full_name',
    )
