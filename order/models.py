from django.db import models
from registration.models import CustomUser
from product.models import Product


STATUS = (
    ('delivered', 'delivered'),
    ('undelivered', 'undelivered'),
)

# Create your models here.
class Delivery(models.Model):
    user      = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name      = models.CharField(max_length=100)
    country   = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city      = models.CharField(max_length=100)
    state     = models.CharField(max_length=100)
    contact   = models.CharField(max_length=100)
    sub_id    = models.CharField(max_length=100)
    date      = models.DateTimeField(editable=False, auto_now_add=True, auto_created=True)
    product   = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity  = models.CharField(max_length=100)
    delivery  = models.CharField(choices=STATUS, default='undelivered', max_length=100)
    status    = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.name.title()} -> {self.product} -> {self.quantity}"