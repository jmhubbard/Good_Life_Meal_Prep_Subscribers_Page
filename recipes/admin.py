from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'proteins', 'carbs', 'fats', 'calories')
    field_display = ('name','description','proteins', 'carbs', 'fats', 'calories', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at',)
    search_fields = ('name',)
    ordering = ('name',)
admin.site.register(Recipe, RecipeAdmin)
