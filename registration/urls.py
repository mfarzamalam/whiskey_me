from django.urls import path, include
from .views import LoginView, RegisterView, PasswordReset, PasswordResetDone, PasswordResetConfirm, PasswordResetComplete
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    path('passwordreset/', PasswordReset.as_view(), name='password_reset'),
    path('passwordresetdone/', PasswordResetDone.as_view(), name='password_reset_done'),
    path('passwordresetconfirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('passwordresetcomplete/', PasswordResetComplete.as_view(), name='password_reset_complete'),
]
