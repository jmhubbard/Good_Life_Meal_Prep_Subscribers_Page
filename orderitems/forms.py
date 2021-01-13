from django import forms
from .models import OrderItem

class OrderItemUpdateForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ('quantity', 'special_requests')

        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control'}),
        }