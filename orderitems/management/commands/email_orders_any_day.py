from django.core.management.base import BaseCommand

from orderitems.utils import emailWeeklyOrders



class Command(BaseCommand):
    help = 'Emails admin an email containing the weekly orders'

    def handle(self, *args, **options):

        emailWeeklyOrders()
        print("Orders have been emailed")

