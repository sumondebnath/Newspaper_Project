from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=80, widget=forms.TextInput(attrs={"placeholder":"Username"}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder":"First Name"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder":"Last Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]