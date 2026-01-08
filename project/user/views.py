from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail
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
            return redirect('home')

    return render(request, 'users/register.html', {'form': form})


def home_view(request):
    return render(request, 'users/home.html')


def admin_email(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            send_mail(
                subject = "Нова реєстрація на сайті",
                message = f"Новий користувач: {user.username} | Email: {user.email}",
                from_email= 'test@test.com',
                recipient_list = ['admin@example.com'],
            )
            return redirect('home')












