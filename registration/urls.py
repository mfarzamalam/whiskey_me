from django.urls import path, include
from .views import LoginView, RegisterView
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
