from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, fields, widgets
from django.contrib.auth.forms import (UserCreationForm,PasswordResetForm,SetPasswordForm)
from .models import CustomUser


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-input col-12 my-1 '
        self.fields['email'].widget.attrs['placeholder'] = 'Email address'
        self.fields['password1'].widget.attrs['class'] = 'form-input col-12 my-1 '
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'form-input col-12 my-1 '
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')


class UserLoginForm(forms.Form):
    email=forms.EmailField(max_length=256, required=True,widget=forms.EmailInput(attrs={'class': 'form-input col-12 my-1 ', 'name': 'email','placeholder':'Email address'}))
    password=forms.CharField(max_length=128,required=True,widget=forms.PasswordInput(attrs={'class': 'form-input col-12 my-1 ', 'name': 'password','placeholder':'Password'}))