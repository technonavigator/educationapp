from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from . import forms


def auth(request):
    if request.method == 'POST':
        form = forms.SignInForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=password)
            login(request, user)
            return redirect('home/')

    else:
        form = forms.SignInForm()
    return render(request, 'main/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/home')
    else:
        form = forms.SignUpForm()
    return render(request, 'main/register.html', {'form': form})

def logout(request):
    pass

def home(request):
    return render(request, 'main/home.html')
