from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)