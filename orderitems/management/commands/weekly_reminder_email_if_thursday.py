from django.core.management.base import BaseCommand


from orderitems.utils import weekly_reminder_email

import datetime


class Command(BaseCommand):
    help = 'Emails admin an email containing the weekly orders'

    def handle(self, *args, **options):
        current_day_of_the_week = datetime.datetime.today().weekday()

        if current_day_of_the_week == 3:
            weekly_reminder_email()
            print("Users have been emailed weekly reminder")
        else:
            print("Today is not Thursday")
