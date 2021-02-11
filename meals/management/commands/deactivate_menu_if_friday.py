from django.core.management.base import BaseCommand
from django.db import IntegrityError
import datetime


from meals.models import Meal


class Command(BaseCommand):
    help = 'Deactivates the current menu so users cannot update their orders.'

    def handle(self, *args, **options):
        current_day_of_the_week = datetime.datetime.today().weekday()

        if current_day_of_the_week == 4:
            all_meals = Meal.objects.all()
            for meal in all_meals:
                if meal.is_on_menu:
                    meal.on_last_weeks_menu = True
                    meal.is_on_menu = False
                    meal.save()
                else:
                    meal.on_last_weeks_menu = False
                    meal.save()
            print("Menu has been deactivated and last weeks menu has been recorded.")
        else:
            print("Menu is still active")
