import re
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder": "Email",
            "autocomplete": "email",
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "id": "id_password",
            "autocomplete": "new-password",
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Confirm password",
            "id": "id_confirm_password",
            "autocomplete": "new-password",
        })
    )
    agree_terms = forms.BooleanField(
        required=True,
        error_messages={
            "required": "You must agree with the Terms to continue."
        },
    )

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if (
            User.objects.filter(email__iexact=email).exists()
            or User.objects.filter(username__iexact=email).exists()
        ):
            raise forms.ValidationError("An account with this email already exists.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get("password", "")
        if len(password) < 12:
            raise forms.ValidationError("Your password must be at least 12 characters long.")
        if not re.search(r"\d", password) or not re.search(r"[^A-Za-z0-9]", password):
            raise forms.ValidationError(
                "Your password must contain at least one number and one special symbol."
            )
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")
        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder": "Email",
            "autocomplete": "email",
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "id": "id_login_password",
            "autocomplete": "current-password",
        })
    )
    remember_me = forms.BooleanField(required=False)