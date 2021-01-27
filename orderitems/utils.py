import os
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse

from django.contrib.sites.models import Site
import datetime



from users.models import User
from orderitems.models import OrderItem

def emailWeeklyOrders():
    all_users = User.objects.filter(is_active=True)
    orders = []

    for customer in all_users:
        orderItems = OrderItem.objects.filter(user=customer, is_on_current_menu=True, quantity__gt=0)

        order = {"name": customer.name, "email": customer.email, "phone_number": customer.phone_number.as_national, "street_address": customer.street_address, "city": customer.city, "state": customer.state, "zipcode": customer.zip_code, "meals": orderItems}
        orders.append(order)

    domain = Site.objects.get_current().domain

    user_login_path = reverse('login')
    user_url = f'http://{domain}{user_login_path}'

    current_date = datetime.date.today()
    
    context = {
        "orders": orders,
        "user_url": user_url,
        "current_date": current_date,

    }
    message_text = render_to_string("orderitems/email_weekly_orders.txt", context=context)
    message_html = render_to_string("orderitems/email_weekly_orders.html", context=context)


    current_admins = User.objects.filter(is_admin=True)

    send_mail(
        'Weekly Orders Email',
        message_text,
        os.getenv("EMAIL_HOST_USER"),
        current_admins,
        fail_silently=False,
        html_message=message_html,

    )
