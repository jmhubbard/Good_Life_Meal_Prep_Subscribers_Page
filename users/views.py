from django.shortcuts import render
from django.views.generic.edit import (
        CreateView,
        DeleteView, 
        UpdateView,)
from django.contrib.messages.views import SuccessMessageMixin
from main.decorators import unauthenticated_user
from django.utils.decorators import method_decorator

from django.contrib.auth.views import (
        PasswordChangeView,
        PasswordChangeDoneView,
        PasswordResetView,
        PasswordResetDoneView, 
        PasswordResetConfirmView,
        PasswordResetCompleteView,)



from .models import User
from .forms import UserSignUpForm

class UserSignUpView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserSignUpForm
    success_url = "/accounts/login/"
    success_message = "Your account was successfully created. Log in to update your weekly order."

    @method_decorator(unauthenticated_user) #If user is already authenticated they will be redirected to their subscription
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CustomPasswordChangeView(PasswordChangeView):

    template_name = "users/password_change.html"


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "users/password_change_done.html"


class CustomPasswordResetView(PasswordResetView):

    template_name = "users/password_reset.html"

    @method_decorator(unauthenticated_user) #If user is already authenticated they will be redirected to their subscription page
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CustomPasswordResetDoneView(PasswordResetDoneView):

    template_name = "users/password_reset_sent.html"

    @method_decorator(unauthenticated_user) #If user is already authenticated they will be redirected to their subscription page
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CustomPasswordResetConfirmView(PasswordResetConfirmView):

    template_name = "users/password_reset_form.html"

    @method_decorator(unauthenticated_user) #If user is already authenticated they will be redirected to their subscription page
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CustomPasswordResetCompleteView(PasswordResetCompleteView):

    template_name = "users/password_reset_done.html"

    @method_decorator(unauthenticated_user) #If user is already authenticated they will be redirected to their subscription page
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
