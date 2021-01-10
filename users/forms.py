import string
from django import forms
from django.forms import ModelForm
from django.contrib.auth.password_validation import validate_password

from .models import User

class UserSignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = User
        fields = ('email','name', 'date_of_birth')

    def clean_email(self):
        email = self.cleaned_data['email']
        return email.lower()
        # return email


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        validate_password(password2)
        return password2

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        user.save()
        return user
