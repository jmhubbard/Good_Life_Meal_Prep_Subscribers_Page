from django.db.models.signals import post_save
from django.core.mail import send_mail

from .models import User
from .utils import email_admin_new_user_sign_up


def email_admin_after_create_new_user(sender, instance, created, **kwargs):
    """
    A function that emails admin a notification when a new user signs up on the website.
    """

    if created:
        new_user = instance    
        email_admin_new_user_sign_up(new_user)
        
post_save.connect(email_admin_after_create_new_user, sender=User)

