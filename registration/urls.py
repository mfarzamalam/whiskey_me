from django.urls import path, include
from .views import HomeView, LoginView, ShopView, ProductPageView, RegisterView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/', ProductPageView.as_view(), name='product'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
