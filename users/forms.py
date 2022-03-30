from cProfile import label
from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from django.contrib.auth import password_validation
class UserRegisterForm(UserCreationForm):
    firstname=forms.CharField(required=True)
    lastname=forms.CharField(required=True)

    email=forms.EmailField(required=True)
   
    class Meta:
        model=User
        fields=['firstname','lastname','username','email','password1','password2']

class MyPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(label=("Email"),max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))