from django.contrib import admin
from.models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'created_at', 'updated_at')
    field_display = ('id', 'user','created_at','updated_at')
    readonly_fields = ('created_at', 'updated_at',)
    search_fields = ('user', 'created_at', 'updated_at')
    ordering = ('user',)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'order')
    field_display = ('name','quantity','order')
    # readonly_fields = ('created_at', 'updated_at',)
    search_fields = ('name', 'order')
    ordering = ('name',)

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)