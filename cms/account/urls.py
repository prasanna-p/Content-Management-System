
from django.urls import path,include
from account.views import UserCreation
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView


urlpatterns = [
    # path("",include("django.contrib.auth.urls")),
    path('signup',UserCreation.as_view()),
    path('login/',LoginView.as_view(template_name='account/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout')
]
