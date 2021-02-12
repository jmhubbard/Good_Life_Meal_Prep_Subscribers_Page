from django.core.management.base import BaseCommand
from django.db import IntegrityError


from orderitems.models import OrderItem

import datetime


class Command(BaseCommand):
    help = 'Resets all previous weeks order items quantity to 0 and is_on_current_menu to False'

    def add_arguments(self, parser):
        parser.add_argument('--any_day', action='store_true', help='Runs the function regardless of the day of the week.')


    def handle(self, *args, **options):
        current_day_of_the_week = datetime.datetime.today().weekday()

        if options['any_day']:
            current_day_of_the_week = 6


        if current_day_of_the_week == 6:
            current_menu_order_items = OrderItem.objects.filter(is_on_current_menu=True)
            for item in current_menu_order_items:
                item.quantity = 0
                item.is_on_current_menu = False
                item.save()
            print("Item order quantities have been set to 0")
        else:
            print("Today isn't Sunday so items won't be reset")