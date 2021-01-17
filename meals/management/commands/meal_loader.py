from django.core.management.base import BaseCommand
from django.db import IntegrityError


from meals.models import Meal
from meals.meal_list.meal_list import meal_list


class Command(BaseCommand):
    help = 'Creates meals from meal_list'

    def add_arguments(self, parser):
        parser.add_argument('--save', action='store_true', help='Save meals to the database')

    def handle(self, *args, **options):
        totalAttemptedItems = 0
        #Meal Counts
        savedMealCount = 0
        duplicateMeals = 0

        for item in meal_list:
            totalAttemptedItems += 1
            #Create an instance of Meal using the provided show name
            meal = Meal(
                name = item["name"],
                description = item["description"],
                proteins = item["proteins"],
                carbs = item["carbs"],
                fats = item["fats"],
                calories = item["calories"],
                small_picture_url = item["small_picture_url"],
                large_picture_url = item["large_picture_url"],
                is_on_menu = item["is_on_menu"],
            )
            if options["save"]:
                    try:
                        #Save the show instance if it doesn't exist in database
                        meal.save()
                    except IntegrityError:
                        #If the show already exists then get that shows object to use when saving episodes
                        duplicateMeals += 1
                    else:
                        savedMealCount += 1

        print(f'Total attempted meals: {totalAttemptedItems}')
        #Final Show Counts
        print(f'Total saved meals: {savedMealCount}')
        print(f'Skipped {duplicateMeals} duplicated meals')
