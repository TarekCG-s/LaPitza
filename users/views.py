from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import UserRegistrationForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Thank {username} for making an account')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    context = {
        'form':form,
    }
    return render(request, 'users/register.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('home')
