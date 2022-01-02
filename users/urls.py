"""Defines the URL patterbs for users"""
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import authenticate, login, urls
from django.contrib.auth import views as auth_views

from users import views
app_name = 'users'

urlpatterns = [
    # Login Page
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),

    # Logout Page
    url(r'^logout/$', views.logout_view, name='logout'),

    # Registration page
    url(r'^register/$', views.register, name='register'),

]



