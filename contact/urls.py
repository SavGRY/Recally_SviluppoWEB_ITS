from . import views
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name="contact"

urlpatterns = [
    path(" ", views.ContactFormView.as_view(), name="home_contact")
]