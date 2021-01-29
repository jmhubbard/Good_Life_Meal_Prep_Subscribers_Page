from django.core.management.base import BaseCommand


from orderitems.utils import emailWeeklyOrders

import datetime


class Command(BaseCommand):
    help = 'Emails admin an email containing the weekly orders'

    def handle(self, *args, **options):
        current_day_of_the_week = datetime.datetime.today().weekday()

        if current_day_of_the_week == 4:
            total_emails_sent, current_admins = emailWeeklyOrders()
            print("{} total emails have been sent to {}".format(total_emails_sent, current_admins))
        else:
            print("email_orders_if_friday was run, but today is not Friday so no emails were sent.")
