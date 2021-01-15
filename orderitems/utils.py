import os
from django.core.mail import send_mail
from django.template.loader import render_to_string


from users.models import User
from orderitems.models import OrderItem


def email_test(user, message):
    send_mail(
        'Quote test',
        message,
        os.getenv("EMAIL_HOST_USER"),
        [user],
        fail_silently=False,
    )

def emailWeeklyOrders():
    all_users = User.objects.filter(is_active=True)
    orders = []

    for customer in all_users:
        orderItems = OrderItem.objects.filter(user=customer, is_on_current_menu=True) 
        order = {"name": customer.name, "email": customer.email, "meals": orderItems}
        orders.append(order)

    context = {
        "orders": orders, 
    }
    message_text = render_to_string("orderitems/email_weekly_orders.txt", context=context)

    
    send_mail(
        'Weekly Orders Email',
        message_text,
        os.getenv("EMAIL_HOST_USER"),
        [os.getenv("EMAIL_HOST_USER")],
        fail_silently=False,
    )
