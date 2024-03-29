from django.db.models.signals import post_save

from .models import OrderItem
from meals.models import Meal
from users.models import User


def create_order_items_for_new_user(sender, instance, created, **kwargs):
    """
    A function that creates OrderItems for every Meal in the database for a newly created User. If the meal is currently on the menu, the
    Orderitem.is_on_current_menu will be set to True. Otherwise it's set to False. This allows users
    who sign 
    """

    if created:
        all_current_meals = Meal.objects.filter(is_on_menu=True)
        for item in all_current_meals:
            OrderItem.objects.create(user=instance, item=item, is_on_current_menu=True)
        all_not_current_meals = Meal.objects.filter(is_on_menu=False)
        for food in all_not_current_meals:
            OrderItem.objects.create(user=instance, item=food, is_on_current_menu=False)

post_save.connect(create_order_items_for_new_user, sender=User)

def create_order_items_for_new_meal(sender, instance, created, **kwargs):
    """
    A function that creates a new OrderItem for every user currently in the database, when a new meal
    is created.
    """

    if created:
        all_users = User.objects.all()
        for person in all_users:
            OrderItem.objects.create(user=person, item=instance)

post_save.connect(create_order_items_for_new_meal, sender=Meal)
