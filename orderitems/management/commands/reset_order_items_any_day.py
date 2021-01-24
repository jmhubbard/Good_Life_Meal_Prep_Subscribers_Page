from django.core.management.base import BaseCommand
from django.db import IntegrityError


from orderitems.models import OrderItem



class Command(BaseCommand):
    help = 'Resets all previous weeks order items quantity to 0 and is_on_current_menu to False'

    def handle(self, *args, **options):

        current_menu_order_items = OrderItem.objects.filter(is_on_current_menu=True)
        for item in current_menu_order_items:
            item.quantity = 0
            item.is_on_current_menu = False
            item.save()
