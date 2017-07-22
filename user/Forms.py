from django import forms
from django.contrib.auth.models import User
from django.forms.models import ValidationError


class Login(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)


class Registration(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email need to be unique")

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if not password == confirm_password:
            raise ValidationError("Confirmation password doesn't match")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
