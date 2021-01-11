from django.contrib import admin

from orderitems.models import OrderItem


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'quantity', 'special_requests', 'is_on_current_menu', 'updated_at')
    field_display = ('user', 'item', 'quantity', 'special_requests', 'is_on_current_menu', 'updated_at')
    readonly_fields = ('updated_at',)
    search_fields = ('user', 'item')
    ordering = ('user',)

admin.site.register(OrderItem, OrderItemAdmin)
