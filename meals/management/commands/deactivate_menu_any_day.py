from django.core.management.base import BaseCommand
from django.db import IntegrityError


from meals.models import Meal


class Command(BaseCommand):
    help = 'Deactivates the current menu so users cannot update their orders.'

    def handle(self, *args, **options):

        current_menu = Meal.objects.filter(is_on_menu=True)
        for item in current_menu:
            item.is_on_menu = False
            item.save()
        print("Menu has been deactivated")
