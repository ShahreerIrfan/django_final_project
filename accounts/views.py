from django.shortcuts import render,redirect
from .forms import RegistrationForm


# Create your views here.

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('cart')
    return render(request, 'accounts/register.html', {'form':form})

def profile(request):
    return render(request,'accounts/dashboard.html')

def singin(request):
    return render(request,'accounts/signin.html')