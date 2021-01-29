import os

from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse


def send_email(context, message_text, message_html, subject, recipient_list):

    message_text = render_to_string(message_text, context=context)
    message_html = render_to_string(message_html, context=context)

    return send_mail(
        subject,
        message_text,
        os.getenv("EMAIL_HOST_USER"),
        recipient_list,
        fail_silently=False,
        html_message=message_html,
    )


def get_login_url():
    domain = Site.objects.get_current().domain
    user_login_path = reverse('login')
    user_login_url = f'http://{domain}{user_login_path}'
    return user_login_url

def get_admin_login_url():
    domain = Site.objects.get_current().domain
    admin_login_path = reverse('admin:index')
    admin_login_url = f'http://{domain}{admin_login_path}'
    return admin_login_url

