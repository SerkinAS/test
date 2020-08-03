from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import MyForm


def register(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = MyForm()
    return render(request, 'registration/register.html', {'form': form})


def signout(request):
    auth.logout(request)
    return render(request, 'registration/logout.html')