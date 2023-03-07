from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField

from .models import User


class CustomUserCreationForm(UserCreationForm):
    username = UsernameField(
        label="Nazwa użytkownika", help_text="", widget=forms.TextInput
    )
    email = forms.EmailField(label="Email", help_text="", widget=forms.EmailInput)
    password1 = forms.CharField(label="Hasło", help_text="", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Powtórz hasło", help_text="", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
        }
        help_texts = {
            "username": None,
            "email": None,
            "password1": None,
            "password2": None,
        }
