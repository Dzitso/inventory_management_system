from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        # Check if the password contains at least 8 characters
        if len(password1) < 8:
            raise ValidationError("Your password must contain at least 8 characters.")

        # Check if the password is entirely numeric
        if password1.isdigit():
            raise ValidationError("Your password can't be entirely numeric.")

        # Check if the password is a commonly used password
        # You can use a library like `zxcvbn` to check for common passwords

        return password1

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')