from django import forms
from django.utils.translation import gettext_lazy as _

from users.models import User

from django.contrib.auth.forms import UsernameField

from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.utils.text import capfirst

from django.core.exceptions import ValidationError

from django.core.mail import send_mail
import os



UserModel = get_user_model()


class CustomAuthenticationForm(forms.Form):
    """
    A custom authentication class that copys itself from Djangos AuthenticationForm, which is the 
    form_class used by the generic LoginView. A class of 'form-control' has been added to each widget
    to allow for Bootstrap styling.
    """

    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
    )

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

        # Set the max length and label for the "username" field.
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        username_max_length = self.username_field.max_length or 254
        self.fields['username'].max_length = username_max_length
        self.fields['username'].widget.attrs['maxlength'] = username_max_length
        if self.fields['username'].label is None:
            self.fields['username'].label = capfirst(self.username_field.verbose_name)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={'username': self.username_field.verbose_name},
        )

class ContactForm(forms.Form):
    subjectchoices = (
        ('Problems updating my order','Problems updating my order'),
        ("Issues updating my account information", "Issues updating my account information"),
        ('Cancel this weeks order','Cancel this weeks order'),
        ('Cancel my current membership','Cancel my current membership'),
        ('Other','Other')
    )

    subject = forms.ChoiceField(choices= subjectchoices, widget=forms.Select(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    def send_message(self, current_user):
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        recipient_list = [os.getenv("EMAIL_HOST_USER")]
        
        mailmessage = (f'Sender: {current_user.name}\nEmail: {current_user.email}\nMessage: {message}')

        send_mail(
            f'The Good Life Meal Prep Subscribers Comment Form: {subject}',
            mailmessage,
            os.getenv("EMAIL_HOST_USER"),
            recipient_list,
            fail_silently=False
        )