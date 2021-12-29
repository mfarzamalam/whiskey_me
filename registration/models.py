from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.signals import post_save
import stripe
# from partners.models import Category

from whiskey_me.stripe_key import SECRET_KEY
stripe.api_key = SECRET_KEY


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    stripe_id = models.CharField(max_length=100)

    def __str__(self):
        return self.email



def post_save_customerUser(sender, instance, created, *args, **kwargs):
    if created:
        CustomUser.objects.get_or_create(email=instance)

    user, created = CustomUser.objects.get_or_create(email=instance)
    
    if user.stripe_id is None or user.stripe_id == '':
        user_stripe_id = stripe.Customer.create(email=instance.email)
        user.stripe_id = user_stripe_id.id
        user.save()

post_save.connect(post_save_customerUser, sender=CustomUser)