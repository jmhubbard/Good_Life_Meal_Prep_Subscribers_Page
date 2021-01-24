from django.core.management.base import BaseCommand


from orderitems.utils import emailWeeklyOrders

import datetime


class Command(BaseCommand):
    help = 'Emails admin an email containing the weekly orders'

    def handle(self, *args, **options):
        current_day_of_the_week = datetime.datetime.today().weekday()

        if current_day_of_the_week == 4:
            emailWeeklyOrders()
            print("Orders have been emailed")
        else:
            print("Today is not Friday")
