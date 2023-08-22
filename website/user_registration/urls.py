
from django.contrib import admin
from django.urls import path
from user_registration import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('login', views.login, name='login'),
]
