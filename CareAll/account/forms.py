from django import forms
from account.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):

    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:

        model = User
        Fields = ("username","password1","password2","email","firstname","lastname")