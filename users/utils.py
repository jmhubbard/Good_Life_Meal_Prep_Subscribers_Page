from .models import User
from main.utils import get_admin_login_url, get_login_url, send_email


def get_all_active_users():
    """
    Returns a queryset of all active users.
    """
    all_users = User.objects.filter(is_active=True)
    return all_users


def get_all_admins():
    """
    Returns a queryset of all active admin users.
    """
    current_admins = User.objects.filter(is_admin=True, is_active=True)
    return current_admins


def email_admin_new_user_sign_up(new_user):
    """
    Sends an email to all the admins that a new user has signed up on the platform.
    """
    admin_login_url = get_admin_login_url()
    user_login_url = get_login_url()

    context = {
        "new_user": new_user,
        "admin_login_url": admin_login_url,
        "user_login_url": user_login_url,
    }
    message_text = "users/email_admin_new_user_signup.txt"
    message_html = "users/email_admin_new_user_signup.html"
    subject = "The Good Life Meal Prep Subscribers New User Signup Notification"
    current_admins = get_all_admins()
    current_admins_emails = [admin.email for admin in current_admins]

    send_email(context=context, message_text=message_text, message_html=message_html, subject=subject, recipient_list=current_admins_emails)

