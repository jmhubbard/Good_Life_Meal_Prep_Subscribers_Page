import os
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.sites.models import Site

from .models import User


def email_admin_new_user_sign_up(new_user):
    
    domain = Site.objects.get_current().domain
    path = reverse('admin:index')
    url = f'http://{domain}{path}'
    
    recipient_list = User.objects.filter(is_admin=True)
    
    context = {
        "new_user": new_user,
        "admin_link": url,
    }

    message_text = render_to_string("users/email_admin_new_user_signup.txt", context=context)
    message_html = render_to_string("users/email_admin_new_user_signup.html", context=context)
    return send_mail(
        'The Good Life Meal Prep Subscribers New User Signup Notification',
        message_text,
        os.getenv("EMAIL_HOST_USER"),
        recipient_list,
        fail_silently=False,
        html_message=message_html,
    )

