from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from models import UserProfile


class UserSignupForm(UserCreationForm):
    attributes = {
        'class': 'form-control',
        'required': 'required',
        'placeholder': 'Email Address',
    }

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs=attributes)
    )

    attribute = {
        'class': 'form-control',
        'required': 'required',
        'placeholder': 'Username',
        'autofocus': 'autofocus'
    }

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs=attribute)
    )

    attributes['placeholder'] = 'Password'
    password1 = forms.CharField(
        required=True,
        label=_("Password"),
        widget=forms.PasswordInput(attrs=attributes)
    )

    attributes['placeholder'] = 'Confirm Password'
    password2 = forms.CharField(
        required=True,
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs=attributes),
        help_text=_("Enter the same password as above, for verification.")
    )

    attributes['placeholder'] = 'First Name'
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs=attributes)
    )

    attributes['placeholder'] = 'Last Name'
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs=attributes)
    )

    attributes['placeholder'] = 'Gender'
    gender = forms.CharField(
        required=True,
        label=_("Gender"),
        widget=forms.Select(
            attrs=attributes,
            choices=UserProfile.GENDER_CHOICES
        )
    )

    attributes['placeholder'] = 'Birthday'
    attributes['type'] = 'date'
    birthday = forms.DateField(
        required=True,
        label=_("Birthday"),
        widget=forms.DateInput(
            attrs=attributes
        )
    )

    def save(self, commit=True):
        user = super(UserSignupForm, self).save(commit=commit)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        profile = UserProfile()
        profile.birthday = self.cleaned_data['birthday']
        profile.gender = self.cleaned_data['gender']
        profile.user = user
        profile.save()
