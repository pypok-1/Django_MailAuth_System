from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import UserForm


def register_user(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'users/register.html', {'form': form})
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')

    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm(request)
        return render(request, 'users/login.html', {'form': form})

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('')

    return render(request, 'users/login.html', {'form': form})








