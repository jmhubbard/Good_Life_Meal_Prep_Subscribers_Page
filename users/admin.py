from django import forms
from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.utils.translation import ngettext

from .models import User


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'name', 'date_of_birth')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        return email
    
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'name', 'password', 'date_of_birth', 'is_active', 'is_admin')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        return email

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    actions = [
    'add_additional_40_meals',
    'add_additional_60_meals',
    'add_additional_80_meals',
    'change_current_meals_to_60_meals',
    'change_current_meals_to_80_meals',
    ]

    def add_additional_40_meals(self, request, queryset):
        total = 0
        for user in queryset:
            user.remaining_meals += 40
            user.save()
            total += 1
        self.message_user(request, ngettext(
        '40 meals were added to %d user.',
        '40 meals were added to %d users.',
        total,
        ) % total, messages.SUCCESS)

    def add_additional_60_meals(self, request, queryset):
        total = 0
        for user in queryset:
            user.remaining_meals += 60
            user.save()
            total += 1
        self.message_user(request, ngettext(
        '60 meals were added to %d user.',
        '60 meals were added to %d users.',
        total,
        ) % total, messages.SUCCESS)


    def add_additional_80_meals(self, request, queryset):
        total = 0
        for user in queryset:
            user.remaining_meals += 80
            user.save()
            total += 1
        self.message_user(request, ngettext(
        '80 meals were added to %d user.',
        '80 meals were added to %d users.',
        total,
        ) % total, messages.SUCCESS)


    def change_current_meals_to_60_meals(self, request, queryset):
        total = 0
        for user in queryset:
            user.remaining_meals = 60
            user.save()
            total += 1
        self.message_user(request, ngettext(
        '%d user had their meal subscription changed to 60 meals.',
        '%d users had their meal subscriptions changed to 60 meals.',
        total,
        ) % total, messages.SUCCESS)


    def change_current_meals_to_80_meals(self, request, queryset):
        total = 0
        for user in queryset:
            user.remaining_meals = 80
            user.save()
            total += 1
        self.message_user(request, ngettext(
        '%d user had their meal subscription changed to 80 meals.',
        '%d users had their meal subscriptions changed to 80 meals.',
        total,
        ) % total, messages.SUCCESS)

    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'name','date_of_birth', 'remaining_meals', 'is_admin', 'updated_at', 'is_active')
    list_filter = ('is_admin', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'date_of_birth', 'phone_number')}),
        ('Delivery Address', {'fields': ('street_address', 'city', 'state', 'zip_code')}),
        ('Remaining Meals In Current Plan', {'fields': ('remaining_meals',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'groups')}),
        ('Dates', {'fields': ('created_at','updated_at',)})
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'date_of_birth', 'phone_number', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    readonly_fields = ('created_at', 'updated_at',)


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
# admin.site.unregister(Group)