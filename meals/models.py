from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    proteins = models.PositiveSmallIntegerField(null=True, blank=True)
    carbs = models.PositiveSmallIntegerField(null=True, blank=True)
    fats = models.PositiveSmallIntegerField(null=True, blank=True)
    calories = models.PositiveSmallIntegerField(null=True, blank=True)
    large_picture_url = models.URLField(null=True, blank=True)
    menu_sort_order = models.PositiveSmallIntegerField(default=0)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_on_menu = models.BooleanField(default=False)



    def __str__(self):
        return self.name