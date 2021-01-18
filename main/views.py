from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from .decorators import unauthenticated_user

from .forms import CustomAuthenticationForm, ContactForm

from django.contrib.auth.views import (LoginView, LogoutView)

from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic.edit import FormView

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from users.models import User




class HomePageView(TemplateView):
    """
    The homepage view that just include a signup button and some explanitory text.
    """

    template_name = "main/home.html"

    @method_decorator(unauthenticated_user) #If user is already authenticated they will be redirected to their subscription page
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class UserLoginView(LoginView):
    """
    The login view for unauthenticated users. If a user is already authenticated,
    they will be redirected to the menu page.
    """

    form_class = CustomAuthenticationForm
    template_name = "registration/login.html"

    @method_decorator(unauthenticated_user) #If user is already authenticated they will be redirected to their subscription page
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class UserLogoutView(LogoutView):
    """
    A generic logout view that redirects users to the homepage after logging them out.
    """

    next_page = 'home'


class ContactFormView(SuccessMessageMixin, LoginRequiredMixin, FormView):
    template_name = "main/contact_form.html"
    form_class = ContactForm
    success_url = reverse_lazy('contact_form')
    success_message = "Thank you for contacting us. We value your feedback. Somebody will reply within 24 hours."

    def form_valid(self, form):
        current_user = User.objects.get(email=self.request.user)
        form.send_message(current_user)
        return super().form_valid(form)


