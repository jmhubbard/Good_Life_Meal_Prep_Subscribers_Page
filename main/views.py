from django.shortcuts import render

from django.contrib.auth.views import (LoginView,)

class UserLoginView(LoginView):

    template_name = "registration/login.html"

    # @method_decorator(unauthenticated_user) #If user is already authenticated they will be redirected to their subscription page
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)