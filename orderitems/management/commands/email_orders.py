import os

from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.core.mail import send_mail


from meals.models import Meal
from meals.meal_list.meal_list import meal_list
from orderitems.utils import email_test


class Command(BaseCommand):
    help = 'Emails admin an email containing the weekly orders'

    def handle(self, *args, **options):
        user = "jasonhubb@gmail.com"
        message = "Test"

        email_test(user, message)
