from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext

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
        'make_meals_active',
        'make_meals_inactive',
        'create_orderItem'
    ]

    def create_orderItem(self, request, queryset):
        all_users = User.objects.all()
        for user in all_users:
            user_orderItems = user.order_item.all()
            for meal in queryset:
                if meal not in user_orderItems:
                    OrderItem.objects.create(user=user, item=meal)



    def make_meals_active(self, request, queryset):
        total = 0
        for meal in queryset:
            meal.is_active = True
            meal.save()
            total+=1
        self.message_user(request, ngettext(
        '%d meal was successfully made active.',
        '%d meals were successfully made active.',
        total,
    ) % total, messages.SUCCESS)

    def make_meals_inactive(self, request, queryset):
        total = 0
        for meal in queryset:
            meal.is_active = False
            meal.save()
            total +=1
        self.message_user(request, ngettext(
        '%d meal was successfully made inactive.',
        '%d meals were successfully made inactive.',
        total,
    ) % total, messages.SUCCESS)


    list_display = ('is_active', 'name', 'description', 'proteins', 'carbs', 'fats', 'calories')
    field_display = ('name','description','proteins', 'carbs', 'fats', 'calories', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at',)
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Meal, MealAdmin)
