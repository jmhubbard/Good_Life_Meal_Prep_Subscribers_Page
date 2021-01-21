from django.core.management.base import BaseCommand
from django.db import IntegrityError

from orderitems.models import OrderItem
from users.models import User

import datetime

class Command(BaseCommand):
    help = 'Updates all users remaining meal totals after the current weeks order'

    def handle(self, *args, **options):
        current_day_of_the_week = datetime.datetime.today().weekday()

        if current_day_of_the_week == 6:
            all_users = User.objects.filter(is_active=True)

            for user in all_users:
                number_of_meals_ordered = 0
                weekly_order = OrderItem.objects.filter(user=user, is_on_current_menu=True)
                for item in weekly_order:
                    number_of_meals_ordered += item.quantity
                user.remaining_meals -= number_of_meals_ordered
                try:
                    user.save()
                except IntegrityError:
                    user.remaining_meals = 0
                    user.save()
                    print("User went over meals")
        else:
            print("Today isn't Sunday so remaining meals won't be calculated")