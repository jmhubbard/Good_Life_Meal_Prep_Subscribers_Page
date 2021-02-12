import datetime

from django.core.management.base import BaseCommand

from orderitems.utils import emailWeeklyOrders, weekly_order_confirmation_email


class Command(BaseCommand):
    help = 'Emails admin an email containing the weekly orders if it is friday in UTC timezone'

    def add_arguments(self, parser):
        parser.add_argument('--any_day', action='store_true', help='Sends email regardless of the day of the week')


    def handle(self, *args, **options):
        #Monday=0, Tuesday=1, Wednesday=2, Thursday=3, Friday=4, Saturday=5, Sunday=6
        current_day_of_the_week = datetime.datetime.today().weekday()

        if options['any_day']:
            current_day_of_the_week = 4

        if current_day_of_the_week == 4:
            total_emails_sent, current_admins = emailWeeklyOrders()
            print("{} order emails have been sent to this list of admins: {}".format(total_emails_sent, current_admins))

            total_user_emails_sent, total_full_orders, total_empty_orders = weekly_order_confirmation_email()
            print("{} total order confirmations have been sent".format(total_user_emails_sent))
            print("{} users placed an order".format(total_full_orders))
            print("{} users did not place an order".format(total_empty_orders))
        else:
            print("email_orders_if_friday was run, but today is not Friday so no emails were sent.")
