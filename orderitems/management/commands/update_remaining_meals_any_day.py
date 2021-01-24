from django.core.management.base import BaseCommand
from django.db import IntegrityError

from orderitems.models import OrderItem
from users.models import User


class Command(BaseCommand):
    help = 'Updates all users remaining meal totals after the current weeks order'

    def handle(self, *args, **options):
            
        all_users = User.objects.filter(is_active=True)

        for user in all_users:
            number_of_meals_ordered = 0
            weekly_order = OrderItem.objects.filter(user=user, is_on_current_menu=True, quantity__gt=0)
            for item in weekly_order:
                number_of_meals_ordered += item.quantity
            user.remaining_meals -= number_of_meals_ordered
            try:
                user.save()
            except IntegrityError:
                user.remaining_meals = 0
                user.save()
                print("User went over meals")
