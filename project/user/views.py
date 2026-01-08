from email.message import EmailMessage
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
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
            send_mail(
                subject="Нова реєстрація на сайті",
                message=f"Новий користувач: {user.username} | Email: {user.email}",
                from_email='test@test.com',
                recipient_list=['admin@example.com'],
            )
            html_content = render_to_string(
                'emails/user_welcome.html',
                {'username': user.username}
            )
            email = EmailMessage(
                subject="Ласкаво просимо!",
                body=html_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[user.email],
                cc=[settings.ADMIN_EMAIL],
                bcc=[settings.ADMIN_EMAIL],
            )
            email.content_subtype = "html"
            email.send()
            return redirect('home')

    return render(request, 'users/register.html', {'form': form})


def home_view(request):
    return render(request, 'users/home.html')
