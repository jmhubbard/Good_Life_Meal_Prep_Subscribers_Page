from django.core.management.base import BaseCommand

from orderitems.utils import create_weekly_order_csv, email_weekly_orders_csv, weekly_order_confirmation_email


class Command(BaseCommand):
    help = 'Updates all users remaining meal totals after the current weeks order'

    def handle(self, *args, **options):
        create_weekly_order_csv()
        total_emails_sent, current_admins_emails = email_weekly_orders_csv()
        print("{} order emails have been sent to this list of admins: {}".format(total_emails_sent, current_admins_emails))

        total_user_emails_sent, total_full_orders, total_empty_orders = weekly_order_confirmation_email()
        print("{} total order confirmations have been sent".format(total_user_emails_sent))
        print("{} users placed an order".format(total_full_orders))
        print("{} users did not place an order".format(total_empty_orders))
