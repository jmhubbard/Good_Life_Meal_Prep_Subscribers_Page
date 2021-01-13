from django import forms
from .models import OrderItem

from django.core.exceptions import ValidationError


class OrderItemUpdateForm(forms.ModelForm):
    """
    A form that allows users to update a specific OrderItem. Widgets are defined for each field
    so a 'form-control' class can be added to each field to allow for Bootstrap styling. The form
    validates the the quantity amount and doesn't allow numbers greater than 50.
    """

    class Meta:
        model = OrderItem
        fields = ('quantity', 'special_requests')

        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity > 50:
            raise forms.ValidationError("Quantity must be less than 50")
        else:
            return quantity