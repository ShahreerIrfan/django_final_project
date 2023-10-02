from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

def registration(request):
    return render(request,'accounts/register.html')

def profile(request):
    return render(request,'accounts/dashboard.html')

def singin(request):
    return render(request,'accounts/signin.html')