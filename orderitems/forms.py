from django import forms
from .models import OrderItem

from django.core.exceptions import ValidationError


class OrderItemUpdateForm(forms.ModelForm):
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

