from django.core.management.base import BaseCommand

from orderitems.utils import emailWeeklyOrders



class Command(BaseCommand):
    help = 'Emails admin an email containing the weekly orders'

    def handle(self, *args, **options):

        total_emails_sent, current_admins = emailWeeklyOrders()
        print("{} total emails have been sent to {}".format(total_emails_sent, current_admins))

