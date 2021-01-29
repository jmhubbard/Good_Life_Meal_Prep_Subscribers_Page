from django.core.management.base import BaseCommand


from orderitems.utils import weekly_reminder_email

import datetime


class Command(BaseCommand):
    help = 'Emails admin an email containing the weekly orders'

    def handle(self, *args, **options):
        total_emails_sent = weekly_reminder_email()
        print("{} reminder emails have been sent".format(total_emails_sent))
