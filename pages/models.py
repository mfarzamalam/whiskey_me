from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=60 ,null=False,blank=False)
    email= models.EmailField(null=False,blank=False)
    subject = models.CharField(max_length=60 ,null=False,blank=False)
    message = models.TextField(max_length=300 ,null=False,blank=False)
    review_date=models.DateField(auto_now=True)