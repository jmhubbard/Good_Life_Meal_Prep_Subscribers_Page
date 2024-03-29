from django.contrib import admin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ngettext

from .models import Meal
from users.models import User
from orderitems.models import OrderItem


class MealAdmin(admin.ModelAdmin):
    actions = [
        'add_meals_to_menu',
        'remove_meals_from_menu',
        'set_menu_sort_order_to_zero',
    ]

    def add_meals_to_menu(self, request, queryset):
        total = 0
        all_customers = User.objects.all()
        for meal in queryset:
            meal.is_on_menu = True
            meal.save()
            total+=1
            for customer in all_customers:
                try:
                    current_orderItem = OrderItem.objects.get(user=customer, item=meal)
                    current_orderItem.is_on_current_menu = True
                    current_orderItem.save()
                except ObjectDoesNotExist:
                    OrderItem.objects.create(user=customer, item=meal, is_on_current_menu=True)
        self.message_user(request, ngettext(
        '%d meal was successfully added to the menu.',
        '%d meals were successfully added to the menu.',
        total,
        ) % total, messages.SUCCESS)

    def remove_meals_from_menu(self, request, queryset):
        total = 0
        for meal in queryset:
            meal.is_on_menu = False
            meal.save()
            total +=1
            all_orderItems_for_current_meal = OrderItem.objects.filter(item=meal)
            for current_orderItem in all_orderItems_for_current_meal:
                current_orderItem.is_on_current_menu = False
                current_orderItem.quantity = 0
                current_orderItem.save()
        self.message_user(request, ngettext(
        '%d meal was successfully removed from the menu.',
        '%d meals were successfully removed from the menu',
        total,
    ) % total, messages.SUCCESS)

    def set_menu_sort_order_to_zero(self, request, queryset):
        total = 0
        for meal in queryset:
            meal.menu_sort_order = 0
            meal.save()
            total += 1
        
        self.message_user(request, ngettext(
        '%d meals menu sort order was set to empty.',
        '%d meals menu sort order was set to empty.',
        total,
    ) % total, messages.SUCCESS)

    list_display = ('name', 'is_on_menu', 'menu_sort_order', 'description', 'proteins', 'carbs', 'fats', 'calories')
    list_filter = ('is_on_menu','on_last_weeks_menu')
    field_display = ('name','description','proteins', 'carbs', 'fats', 'calories', 'menu_sort_order', 'large_picture_url', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at', 'is_on_menu', 'on_last_weeks_menu')
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Meal, MealAdmin)
