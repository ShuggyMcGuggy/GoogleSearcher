"""Defines the URL patterbs for users"""
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import authenticate, login, urls
from django.contrib.auth import views as auth_views

from users import views
app_name = 'users'

urlpatterns = [
    # Login Page

    # path(
    #     'change-password/',
    #     auth_views.PasswordChangeView.as_view(template_name='change-password.html'),
    # ),
    #
    # path(
    #     'login/',
    #     auth_views.LoginView.as_view(template_name='login.html'),
    # ),

    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
]



