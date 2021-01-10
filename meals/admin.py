from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from django.core.exceptions import ObjectDoesNotExist

from .models import Meal
from users.models import User
from orderitems.models import OrderItem


def make_meals_active(modeladmin, request, queryset):
    for meal in queryset:
        meal.is_active = True
        meal.save()

def make_meals_inactive(modeladmin, request, queryset):
    for meal in queryset:
        meal.is_active = False
        meal.save()




class MealAdmin(admin.ModelAdmin):
    actions = [
        'add_meals_to_menu',
        'remove_meals_from_menu',
        'create_orderItem'
    ]

    def create_orderItem(self, request, queryset):
        all_users = User.objects.all()
        for user in all_users:
            user_orderItems = user.order_item.all()
            for meal in queryset:
                if meal not in user_orderItems:
                    OrderItem.objects.create(user=user, item=meal)



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
                print(current_orderItem)
                current_orderItem.is_on_current_menu = False
                current_orderItem.save()
        self.message_user(request, ngettext(
        '%d meal was successfully removed from the menu.',
        '%d meals were successfully removed from the menu',
        total,
    ) % total, messages.SUCCESS)


    list_display = ('is_on_menu', 'name', 'description', 'proteins', 'carbs', 'fats', 'calories')
    field_display = ('name','description','proteins', 'carbs', 'fats', 'calories', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at',)
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Meal, MealAdmin)
