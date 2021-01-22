from django.db.models.signals import post_save
import os
from django.core.mail import send_mail

from .models import User



def email_admin_after_create_new_user(sender, instance, created, **kwargs):
    """
    A function that emails admin a notification when a new user signs up on the website.
    """

    if created:
        new_user = instance    
        mailmessage = (f'A new user has signed up on the Good Life Meal Prep Subscribers Page.\nEmail: {new_user}\nName: {new_user.name}\nPhone Number: {new_user.phone_number}')
        recipient_list = User.objects.filter(is_admin=True)
        send_mail(
            f'The Good Life Meal Prep Subscribers New User Signup Notification',
            mailmessage,
            os.getenv("EMAIL_HOST_USER"),
            recipient_list,
            fail_silently=False
        )

post_save.connect(email_admin_after_create_new_user, sender=User)

