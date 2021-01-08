from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    proteins = models.PositiveSmallIntegerField(null=True, blank=True)
    carbs = models.PositiveSmallIntegerField(null=True, blank=True)
    fats = models.PositiveSmallIntegerField(null=True, blank=True)
    calories = models.PositiveSmallIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)



    def __str__(self):
        return self.name