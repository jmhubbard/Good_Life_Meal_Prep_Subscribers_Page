from django.db import models
from users.models import User
from meals.models import Meal

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_item')
    item = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='order_item')
    quantity = models.PositiveSmallIntegerField(default=0)
    special_requests = models.TextField(blank=True)
    is_on_current_menu = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}'s order for {self.item}"
