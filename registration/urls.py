from django.urls import path, include
from .views import HomeView, LoginView, ShopView, ProductPageView, RegisterView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/', ProductPageView.as_view(), name='product'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
