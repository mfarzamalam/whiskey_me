from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages, auth
from django.utils.translation import gettext_lazy as _
from product.models import Category, Product


# Create your views here.

class LoginView(TemplateView):
    template_name = "new_template/login.html"


class HomeView(TemplateView):
    template_name = "new_template/index.html"



class ShopView(View):
    def get(self, request,  *args, **kwargs):
        product = Product.objects.all()
        # get_5cl = Category.objects.get(name='5cl')
        # get_70cl = Category.objects.get(name='70cl')

        # prd_5cl = Product.objects.filter(category=get_5cl)
        # prd_70cl = Product.objects.filter(category=get_70cl)
        # for i in prd_70cl:
        #     print(i.product_name)

        context = {
            'product': product,
            # 'product_1': prd_5cl,
            # 'product_2': prd_70cl,
        }
        # if request.user.is_staff:
        #     return redirect('pages:admin_panel')
        return render(request,'new_template/shop.html',context)



class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        context = {
            'form': form,
        }
        return render(request, 'new_template/register.html', context)


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
            return redirect('home')
        else:
            errorStr = ""
            errorDict = dict(signup_form.errors)
            for i in errorDict:
                errorStr += errorDict[i]
            messages.error(request, errorStr)
            return render(request, 'new_template/register.html', context)




class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        context = {
            'form': form,
        }
        return render(request, 'new_template/login.html', context)

    def post(self, request, *args, **kwargs):
        login_form = UserLoginForm(request.POST)
        context = {
            'form': login_form,
        }
        if login_form.is_valid():
            user = auth.authenticate(
                request, email=request.POST['email'], password=request.POST['password'])
            if not user:
                messages.error(
                    request, _("Please enter a correct email address and password. Note that both fields may be case-sensitive."))
                return render(request, 'new_template/login.html', context)
            auth.login(request, user)
            messages.success(request, _("You are currently logged in"))
            return redirect('home')
        else:
            # messages.error(request, _("Something went wrong. Please try again."))
            return render(request, 'new_template/login.html', context)

