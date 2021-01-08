from django.db import models
from users.models import User
from recipes.models import Recipe

class SubscriptionItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription_item')
    item = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='subscription_item')
    quantity = models.PositiveSmallIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}'s order for {self.item}"
