from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from account.models import UserAccount


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


class ImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-img"}))
    class Meta:
        model = UserAccount
        fields = ["image"]


class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]