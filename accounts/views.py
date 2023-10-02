from django.shortcuts import render

# Create your views here.

def registration(request):
    return render(request,'accounts/register.html')

def profile(request):
    return render(request,'accounts/dashboard.html')

def singin(request):
    return render(request,'accounts/signin.html')