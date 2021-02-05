import datetime

from django.core.management.base import BaseCommand

from orderitems.utils import create_weekly_order_csv, email_weekly_orders_csv, weekly_order_confirmation_email


class Command(BaseCommand):
    help = 'Emails admin an email containing the weekly orders and sends all active users an order confirmation'

    def handle(self, *args, **options):
        current_day_of_the_week = datetime.datetime.today().weekday()

        if current_day_of_the_week == 4:
            create_weekly_order_csv()
            total_emails_sent, current_admins_emails = email_weekly_orders_csv()
            print("{} order emails have been sent to this list of admins: {}".format(total_emails_sent, current_admins_emails))
            
            total_user_emails_sent, total_full_orders, total_empty_orders = weekly_order_confirmation_email()
            print("{} total order confirmations have been sent".format(total_user_emails_sent))
            print("{} users placed an order".format(total_full_orders))
            print("{} users did not place an order".format(total_empty_orders))
        else:
            print("email_orders_with_csv_if_friday was run, but today is not Friday so emails were not sent.")


