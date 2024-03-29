from django.contrib import admin

from orderitems.models import OrderItem


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'quantity', 'special_requests', 'is_on_current_menu', 'updated_at')
    list_filter = ('is_on_current_menu',)
    field_display = ('user', 'item', 'quantity', 'special_requests', 'is_on_current_menu', 'updated_at')
    readonly_fields = ('updated_at',)
    search_fields = ('user__name', 'item__name')
    ordering = ('user',)

admin.site.register(OrderItem, OrderItemAdmin)
