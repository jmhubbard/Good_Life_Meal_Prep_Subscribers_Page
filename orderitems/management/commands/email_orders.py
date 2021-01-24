import os

from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.core.mail import send_mail


from meals.models import Meal
from meals.meal_list.meal_list import meal_list
from orderitems.utils import emailWeeklyOrders

import datetime


class Command(BaseCommand):
    help = 'Emails admin an email containing the weekly orders'

    def handle(self, *args, **options):
        current_day_of_the_week = datetime.datetime.today().weekday()

        if current_day_of_the_week == 6:
            emailWeeklyOrders()
            print("Orders have been emailed")
        else:
            print("Today is not Friday")
