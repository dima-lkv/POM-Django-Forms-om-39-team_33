from django.contrib import admin
from authentication.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'role', 'is_admin']
    list_filter = ['role', 'is_admin']
    search_fields = ['first_name', 'last_name', 'middle_name', 'email']


admin.site.register(CustomUser, CustomUserAdmin)
