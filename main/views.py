from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from .decorators import unauthenticated_user



from django.contrib.auth.views import (LoginView, LogoutView)


class HomePageView(TemplateView):

    template_name = "main/home.html"

    @method_decorator(unauthenticated_user) #If user is already authenticated they will be redirected to their subscription page
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class UserLoginView(LoginView):

    template_name = "registration/login.html"

    # @method_decorator(unauthenticated_user) #If user is already authenticated they will be redirected to their subscription page
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

class UserLogoutView(LogoutView):

    next_page = 'home'