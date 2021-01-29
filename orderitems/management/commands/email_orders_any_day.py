from django.core.management.base import BaseCommand

from orderitems.utils import emailWeeklyOrders, weekly_order_confirmation_email



class Command(BaseCommand):
    help = 'Emails admin an email containing the weekly orders and sends all active users an order confirmation'

    def handle(self, *args, **options):

        total_emails_sent, current_admins = emailWeeklyOrders()
        print("{} order emails have been sent to this list of admins: {}".format(total_emails_sent, current_admins))
        
        total_user_emails_sent, total_full_orders, total_empty_orders = weekly_order_confirmation_email()
        print("{} total order confirmations have been sent".format(total_user_emails_sent))
        print("{} users placed an order".format(total_full_orders))
        print("{} users did not place an order".format(total_empty_orders))

