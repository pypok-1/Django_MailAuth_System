from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']
        def clean(self):
            cleaned_data = super().clean()
            password1 = cleaned_data.get('password')
            password2 = cleaned_data.get('password_confirm')
            if password1 and password2 and password1 != password2:
                self.add_error('password_confirm')

            return cleaned_data
