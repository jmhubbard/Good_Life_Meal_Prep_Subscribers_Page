from django.db import models
from recipes.models import Recipe
from users.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order for {self.user.name} - {self.created_at}'

class OrderItem(models.Model):
    name = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='order_item')
    quantity = models.PositiveSmallIntegerField(null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item')
    

    def __str__(self):
        return f'{self.quantity} orders of {self.name}'