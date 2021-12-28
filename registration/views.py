from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.


class HomeView(TemplateView):
    template_name = "new_template/index.html"



class LoginView(TemplateView):
    template_name = "new_template/login.html"



class ShopView(TemplateView):
    template_name = "new_template/shop.html"



class ProductPageView(TemplateView):
    template_name = "new_template/product-page.html"



class RegisterView(TemplateView):
    template_name = "new_template/register.html"