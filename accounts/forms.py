from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import ugettext_lazy as _


class UserSignupForm(UserCreationForm):
    attributes = {'class': 'form-control', 'required': 'required','placeholder': 'Email Address'}
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs=attributes))

    #attributes['placeholder'] = 'Username'
    #username = forms.CharField(required=True, widget=forms.TextInput(attrs=attributes))

    attribute = {'class': 'form-control', 'required': 'required', 'placeholder': 'Username', 'autofocus':'autofocus'}
    username = forms.CharField(required=True, widget=forms.TextInput(attrs=attribute))

    attributes['placeholder'] = 'Password'
    password1 = forms.CharField(required=True,
                                label=_("Password"),
                                widget=forms.PasswordInput(attrs=attributes))

    attributes['placeholder'] = 'Confirm Password'
    password2 = forms.CharField(required=True,
                                label=_("Password confirmation"),
                                widget=forms.PasswordInput(attrs=attributes),
                                help_text=_("Enter the same password as above, for verification."))

    attributes['placeholder'] = 'First Name'
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs=attributes))

    attributes['placeholder'] = 'Last Name'
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs=attributes))