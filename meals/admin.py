from django.contrib import admin

from .models import Meal

class MealAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'name', 'description', 'proteins', 'carbs', 'fats', 'calories')
    field_display = ('name','description','proteins', 'carbs', 'fats', 'calories', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at',)
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Meal, MealAdmin)
