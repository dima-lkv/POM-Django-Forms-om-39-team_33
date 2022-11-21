from django.contrib import admin
from order.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'created_at', 'plated_end_at', 'end_at']
    list_filter = ['created_at', 'end_at']
    search_fields = ['book']
    raw_id_fields = ['book', 'user']
    readonly_fields = ['end_at']


admin.site.register(Order, OrderAdmin)
