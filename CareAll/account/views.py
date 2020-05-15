from django.shortcuts import render
from account.forms import SignupForm
from django.views.generic import CreateView
from account.models import User

# Create your views here.
class SignupView(CreateView):

    model = User
    form_class = SignupForm
    success_url = "/profile"