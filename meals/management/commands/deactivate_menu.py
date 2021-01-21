from django.core.management.base import BaseCommand
from django.db import IntegrityError
import datetime


from meals.models import Meal


class Command(BaseCommand):
    help = 'Deactivates the current menu so users cannot update their orders'

    def handle(self, *args, **options):
        current_day_of_the_week = datetime.datetime.today().weekday()

        if current_day_of_the_week == 4:
            current_menu = Meal.objects.filter(is_on_menu=True)
            for item in current_menu:
                item.is_on_menu = False
                item.save()
            print("Menu has been deactivated")
        else:
            print("Menu is still active")