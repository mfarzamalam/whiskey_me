from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, fields, widgets
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm, PasswordResetForm,SetPasswordForm)
from .models import CustomUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation



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


class UserLoginForm(AuthenticationForm):
    username=forms.EmailField(max_length=256, required=True,widget=forms.EmailInput(attrs={'class': 'form-input col-12 my-1 ', 'name': 'email','placeholder':'Email address'}))
    password=forms.CharField(max_length=128,required=True,widget=forms.PasswordInput(attrs={'class': 'form-input col-12 my-1 ', 'name': 'password','placeholder':'Password'}))


class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254,
        widget = forms.EmailInput(attrs={'placeholder':'Enter your email',  'class':'form-input col-12 my-1'})
    )


class NewPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, help_text=password_validation.password_validators_help_text_html(),
        widget = forms.PasswordInput(attrs={'placeholder':'New Password',  'class':'form-input col-12 my-1'}),
    )
    new_password2 = forms.CharField(label=_("Confirm Password"), strip=False,
        widget = forms.PasswordInput(attrs={'placeholder':'Confirm Password',  'class':'form-input col-12 my-1'}),
    )
