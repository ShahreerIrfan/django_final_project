from django.contrib import admin
from django.urls import path,include
from .views import order

urlpatterns = [
    path('order/',order,name='order_complete')
]