import datetime

from django.core.management.base import BaseCommand

from orderitems.utils import (create_weekly_order_csv, email_weekly_orders_csv,
                                get_meal_totals_for_active_users, weekly_order_confirmation_email)
from users.utils import get_all_active_users


class Command(BaseCommand):
    help = 'Emails admin an email containing the weekly orders and sends all active users an order confirmation'

    def add_arguments(self, parser):
        parser.add_argument('--any_day', action='store_true', help='Sends email regardless of the day of the week')

    def handle(self, *args, **options):
        current_day_of_the_week = datetime.datetime.today().weekday()

        if options['any_day']:
            current_day_of_the_week = 4

        if current_day_of_the_week == 4:
            all_active_users = get_all_active_users()
            current_menu_meal_totals = get_meal_totals_for_active_users()

            create_weekly_order_csv(all_active_users= all_active_users,
                                    current_menu_meal_totals = current_menu_meal_totals
                                    )

            total_emails_sent, current_admins_emails = email_weekly_orders_csv(current_menu_meal_totals=current_menu_meal_totals)
            print("{} order emails have been sent to this list of admins: {}".format(total_emails_sent, current_admins_emails))

            total_user_emails_sent, total_full_orders, total_empty_orders = weekly_order_confirmation_email()
            print("{} total order confirmations have been sent".format(total_user_emails_sent))
            print("{} users placed an order".format(total_full_orders))
            print("{} users did not place an order".format(total_empty_orders))
        else:
            print("email_orders_with_csv_if_friday was run, but today is not Friday so emails were not sent.")


