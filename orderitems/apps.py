from django.apps import AppConfig


class OrderitemsConfig(AppConfig):
    name = 'orderitems'

    def ready(self):
        import orderitems.signals