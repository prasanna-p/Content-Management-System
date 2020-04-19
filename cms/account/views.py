from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm 
from account.forms import SignUpForm

# Create your views here.
class UserCreation(CreateView):

    form_class = SignUpForm
    template_name = "account/signup.html"
    success_url = '/stories'