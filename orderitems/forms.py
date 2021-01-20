from django import forms
from .models import OrderItem

from django.core.exceptions import ValidationError


class OrderItemUpdateForm(forms.ModelForm):
    """
    A form that allows users to update a specific OrderItem. Widgets are defined for each field
    so a 'form-control' class can be added to each field to allow for Bootstrap styling. The form
    validates the the quantity amount and doesn't allow numbers greater than 50.
    """
    
    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.request = kwargs.pop('request')
        super(OrderItemUpdateForm, self).__init__(*args, **kwargs)
        self.current_user = self.request.user
        

    class Meta:
        model = OrderItem
        fields = ('quantity', 'special_requests')

        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control'}),
        }




    def clean_quantity(self):
        #The value that was just submited in the form
        quantity = self.cleaned_data['quantity']
        #The value that was initially in the form field
        initial_quantity = self.initial['quantity']

        #Retrieves all of the current users current order quantities, including the initial quanity in this form, and adds them together
        users_order_items = OrderItem.objects.filter(user = self.current_user, item__is_on_menu = True).order_by('item__name')
        current_total_for_week = 0
        for item in users_order_items:
            current_total_for_week += item.quantity

        #The remaining meals left on the current users plan before this weeks order is submitted
        meals_on_plan = self.current_user.remaining_meals

        #The meals that will be left on the users meals plan after the current weeks order is submitted.
        # Doesn't account for newly passed quantity
        meals_remaining_this_week = (meals_on_plan - current_total_for_week)

        #Figure out the difference between the initial quantity and the newly submitted quantity
        difference_between_new_and_initial_values = (quantity - initial_quantity)
        
        #Takes remaining meals this week and subtracts the difference between the new and initial value.
        meals_on_plan_if_submitted = (meals_remaining_this_week - difference_between_new_and_initial_values)

        #Checks to see if quantity is greater than remaining meals on meal plan 
        # or if by sumbiting this form the user would be over their remaining meals with including their current meal order
        if quantity > meals_on_plan or meals_on_plan_if_submitted < 0:
            raise forms.ValidationError(f'You do not have enough meals remaining in your subscription to satisfy your order. Please remove {abs(meals_on_plan_if_submitted)} meals from this weeks order.')
        else:
            return quantity