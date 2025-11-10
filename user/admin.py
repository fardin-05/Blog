from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'phone_number','password', 'is_staff'] # Add custom fields to list display
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}), # Add custom fields to fieldsets
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
