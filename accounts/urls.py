from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('register/',views.registration,name='register'),
    path('profile/',views.profile,name='profile'),
    path('login/',views.singin,name='login'),
]