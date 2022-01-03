from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView
from .forms import UserRegisterForm, UserLoginForm, PasswordResetForm, NewPasswordForm
from django.contrib import messages, auth
from django.contrib.auth import views

from django.utils.translation import gettext_lazy as _


# Create your views here.

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        context = {
            'form': form,
        }
        return render(request, 'new_template/registration/register.html', context)


    def post(self, request, *args, **kwargs):
        signup_form = UserRegisterForm(request.POST)
        context = {
            'form': signup_form,
        }
        email = request.POST['email']
        password = request.POST['password1']
        if signup_form.is_valid():
            signup_form.save()
            user = auth.authenticate(
                request, username=email, password=password)
            auth.login(request, user)
            messages.success(request, _("Thank you for registration"))
            return redirect('pages:home')
        else:
            errorStr = ""
            errorDict = dict(signup_form.errors)
            for i in errorDict:
                errorStr += errorDict[i]
            messages.error(request, errorStr)
            return render(request, 'new_template/registration/register.html', context)




class LoginView(View):
    def get(self, request, *args, **kwargs):
        print("login get")
        form = UserLoginForm()
        context = {
            'form': form,
        }
        return render(request, 'new_template/registration/login.html', context)

    def post(self, request, *args, **kwargs):
        print("login post")
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(request, email=request.POST['email'], password=request.POST['password'])
            if user:
                auth.login(request, user)
                return redirect('pages:home')
            else:
                return redirect('login')

        else:
            context = {
                'form': login_form,
            }
            return render(request, 'new_template/registration/login.html', context)



class PasswordReset(views.PasswordResetView):
    template_name   = 'new_template/registration/password_reset.html' 
    form_class      = PasswordResetForm
    success_url     = reverse_lazy('password_reset_done')



class PasswordResetDone(views.PasswordResetDoneView):
    template_name   = 'new_template/registration/password_reset_done.html'


class PasswordResetConfirm(views.PasswordResetConfirmView):
    template_name   = 'new_template/registration/password_reset_confirm.html'
    form_class      = NewPasswordForm


class PasswordResetComplete(views.PasswordResetCompleteView):
    template_name   = 'new_template/registration/password_reset_complete.html'