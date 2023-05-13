from datetime import date, timedelta

from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm,
                                       UsernameField)

from .models import User


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["birth_date"].widget.attrs["class"] = "form-control"








    username = UsernameField(
        label="Nazwa użytkownika",
        help_text="",
        widget=forms.TextInput(),
    )
    email = forms.EmailField(
        label="Email",
        help_text="",
        widget=forms.EmailInput(),
    )
    password1 = forms.CharField(
        label="Hasło",
        help_text="",
        widget=forms.PasswordInput(),
    )
    password2 = forms.CharField(
        label="Powtórz hasło",
        help_text="",
        widget=forms.PasswordInput(),
    )
    birth_date = forms.DateField(
        input_formats=["%d-%m-%Y"],
        label="Data urodzenia",
        help_text="",
    )

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get("birth_date")
        age = (date.today() - birth_date) // timedelta(days=365.25)
        if age < 18:
            raise forms.ValidationError("Nie masz 18 lat.")
        return birth_date

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "birth_date")
        widgets = {}
        help_texts = {
            "username": None,
            "email": None,
            "password1": None,
            "password2": None,
        }
        label = {
            "username": "Nazwa użytkownika",
            "email": "Email",
            "password1": "Hasło",
            "password2": "Powtórz hasło",
        }


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label="Nazwa użytkownika", help_text="", widget=forms.TextInput
    )
    password = forms.CharField(label="Hasło", help_text="", widget=forms.PasswordInput)

    error_messages = {
        "invalid_login": "Nazwa użytkownika lub hasło są niepoprawne.",
        "inactive": "Konto jest nieaktywne.",
    }

    class Meta:
        model = User
        fields = ("username", "password", "date_of_birth")
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "date_of_birth": forms.DateInput(attrs={"readonly": "true"}),
        }
        help_texts = {
            "username": None,
            "password": None,
        }
        label = {
            "username": "Nazwa użytkownika",
            "password": "Hasło",
        }
