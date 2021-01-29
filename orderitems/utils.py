import datetime
import os

from main.utils import get_login_url, send_email
from orderitems.models import OrderItem
from users.utils import get_all_active_users, get_all_admins


def get_users_order(user):
    """
    Returns a queryset of a specific users current order items that have a quantity greater than 0
    """
    users_order_items = OrderItem.objects.filter(user=user, is_on_current_menu=True, quantity__gt=0)
    return users_order_items


def get_all_users_orders():
    """
    Returns a list containing a dictionary for each active user.
    
    Each dictionary contains the customers name, email, phone_number
    street_address, city, state, zipcode, and a list of all their meals.
    """
    all_customers = get_all_active_users()
    all_orders = []

    for customer in all_customers:
        users_order_items = get_users_order(customer)
        order = {"name": customer.name, "email": customer.email, "phone_number": customer.phone_number.as_national, "street_address": customer.street_address, "city": customer.city, "state": customer.state, "zipcode": customer.zip_code, "meals": users_order_items}
        all_orders.append(order)

    return all_orders


def emailWeeklyOrders():
    """
    Emails all the current admins an email containing every users current order.
    
    Returns total emails sent and the email for every admin.
    """
    all_orders = get_all_users_orders()
    user_login_url = get_login_url()
    current_date = datetime.date.today()
    context = {
        "all_orders": all_orders,
        "user_login_url": user_login_url,
        "current_date": current_date,
    }

    subject = 'Weekly Orders Email'
    message_text = "orderitems/email_weekly_orders.txt"
    message_html = "orderitems/email_weekly_orders.html"
    current_admins = get_all_admins()
    current_admins_emails = [admin.email for admin in current_admins]

    total_emails_sent = send_email(context=context, message_text=message_text, message_html=message_html, subject=subject, recipient_list=current_admins_emails)
    
    return total_emails_sent, current_admins_emails


def weekly_reminder_email():
    """
    Emails every active user a reminder to place their orders by Thursday at 11:59 pm.
    
    If the user has already placed an order, the email will contain what their current
    order is and a reminder that they can edit their order before 11:59 pm.

    Returns total emails sent.
    """
    all_users = get_all_active_users()
    user_login_url = get_login_url()
    subject = "Don't forget to place your orders!"
    message_text = "orderitems/weekly_reminder_email.txt"
    message_html = "orderitems/weekly_reminder_email.html"

    total_emails_sent = 0

    for customer in all_users:
        users_order_items = get_users_order(customer)
        context = {
            "user_login_url": user_login_url,
            "users_order_items": users_order_items,
            "customer": customer,
        }
        
        recipient_list = [customer.email]

        total_emails_sent += send_email(context, message_text, message_html, subject, recipient_list)
    
    return total_emails_sent
