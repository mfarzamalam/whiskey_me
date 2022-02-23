from django.db import models
from registration.models import CustomUser
from product.models import Product


# Create your models here.
STATUS = (
    ('delivered', 'delivered'),
    ('undelivered', 'undelivered'),
)


class Address(models.Model):
    user      = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fname     = models.CharField(max_length=100)
    lname     = models.CharField(max_length=100)
    country   = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    city      = models.CharField(max_length=100)
    state     = models.CharField(max_length=100)
    contact   = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Delivery(models.Model):
    address   = models.ForeignKey(Address, on_delete=models.CASCADE)
    checkout_id = models.CharField(max_length=100)
    session_id = models.CharField(max_length=100)
    date      = models.DateTimeField(editable=False, auto_now_add=True, auto_created=True)
    product   = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity  = models.CharField(max_length=100)
    delivery  = models.CharField(choices=STATUS, default='undelivered', max_length=100)

    def __str__(self):
        return f"{self.session_id}"