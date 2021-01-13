from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.http import Http404

from .models import OrderItem
from .forms import OrderItemUpdateForm

@login_required()
def orderItemsView(request):
    """
    A view that allows authenticated users the ability to view all of their Order Items that are
    currently on the menu.
    """
    
    current_user = request.user
    order_items = OrderItem.objects.filter(user = current_user, item__is_on_menu = True).order_by('item__name')
    current_total = 0
    for item in order_items:
        current_total += item.quantity
    context ={
        'current_user': current_user,
        'order_items': order_items,
        'current_total': current_total,
    }

    return render(request, 'orderitems/menu.html', context)


class OrderItemUpdate(LoginRequiredMixin, UpdateView):
    """
    A view to allow authenticated users the ability to update one of their OrderItems as long
    as the OrderItem.is_on_menu == True
    """

    model = OrderItem
    form_class = OrderItemUpdateForm
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

        if obj.item.is_on_menu == False or current_user != obj.user:
            raise PermissionDenied
        
        return obj


