from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('order/',views.order_complete,name='order_complete'),
    path('place_order/',views.place_order,name='place_order'),
]