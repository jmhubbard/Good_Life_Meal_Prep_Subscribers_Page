import datetime

from django.core.management.base import BaseCommand

from orderitems.utils import weekly_reminder_email


class Command(BaseCommand):
    help = 'Emails aall users a weekly reminder email'

    def add_arguments(self, parser):
        parser.add_argument('--any_day', action='store_true', help='Sends email regardless of the day of the week')


    def handle(self, *args, **options):
        current_day_of_the_week = datetime.datetime.today().weekday()

        if options['any_day']:
            current_day_of_the_week = 3


        if current_day_of_the_week == 3:
            weekly_reminder_email()
            print("Users have been emailed weekly reminder")
        else:
            print("Today is not Thursday")
