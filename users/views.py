from django.shortcuts import render
from django.views.generic.edit import (
        CreateView,
        DeleteView, 
        UpdateView,)
from django.contrib.messages.views import SuccessMessageMixin
from main.decorators import unauthenticated_user
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.urls import reverse
from django.urls import reverse_lazy

from django.core.exceptions import PermissionDenied
from django.http import Http404



from django.contrib.auth.mixins import LoginRequiredMixin




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


class UserProfileUpdateView(UpdateView):

    model = User
    fields = ["name", "date_of_birth"]
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('orderitems')


    def get_object(self, queryset=None):
        """
        Return the object the view is displaying.
        Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
        Subclasses can override this to return any object.
        """
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView
        if queryset is None:
            queryset = self.get_queryset()

        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        # Next, try looking up by slug.
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        # If none of those are defined, it's an error.
        if pk is None and slug is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(("No %(verbose_name)s found matching the query") %
                        {'verbose_name': queryset.model._meta.verbose_name})

        current_user = self.request.user

        if current_user != obj:
            raise PermissionDenied
        
        # if current_user != obj.user:
        #     raise PermissionDenied
        
        return obj

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        """
        Return the object the view is displaying.
        Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
        Subclasses can override this to return any object.
        """
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView
        if queryset is None:
            queryset = self.get_queryset()

        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        # Next, try looking up by slug.
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        # If none of those are defined, it's an error.
        if pk is None and slug is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(("No %(verbose_name)s found matching the query") %
                        {'verbose_name': queryset.model._meta.verbose_name})

        current_user = self.request.user

        if current_user != obj:
            raise PermissionDenied
        
        return obj

