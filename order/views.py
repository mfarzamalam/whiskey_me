from ast import Add, Del
from hashlib import new
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import Delivery, Address
from product.models import Product
from django.utils import timezone
import stripe

from whiskey_me.stripe_key import SECRET_KEY
stripe.api_key = SECRET_KEY


# Create your views here.


class CustomerDeliver(LoginRequiredMixin,View):
    login_url = "/login/"
    def get(self, request, status="", *args, **kwargs):
        if status == "" or status == None:
            items = Delivery.objects.all()
            print(items)
            class_active = "all"
            action = None
        else:
            items  = Delivery.objects.filter(delivery=status)
            action = status
            class_active = status
        
        context = {'items': items, 'class_active':class_active, 'action':action}
        return render(request, 'new_template/dashboard/delivery.html', context)


class CustomerAddressDetials(LoginRequiredMixin, View):
    login_url = "/login/"
    def get(self, request, pk, *args, **kwargs):
        items  = Delivery.objects.get(pk=pk)
        context = {
            'item':items
        }

        return render(request, 'new_template/dashboard/order_details.html', context)


class changeStatus(LoginRequiredMixin, View):
    login_url = "/login/"
    def post(self, request, pk, *args, **kwargs):
        status = request.POST.get('status')
        item = Delivery.objects.get(pk=pk)
        item.delivery = status
        item.save()

        return redirect('order:deliver')


def test(request):
    print(Delivery.objects.all().count())


def CreateDelivery(request, id, pk, quan, order_type):
    if request.user.is_authenticated:
        Delivery.objects.create(
            address   = Address.objects.filter(user=request.user).first(),
            sub_id    = id,
            date      = timezone.now(),
            product   = Product.objects.filter(pk=pk).first(),
            quantity  = quan,
            delivery  = 'undelivered',
        )
        return HttpResponseRedirect(f'/orders/payment-successful/{id}/{order_type}/')


def paymentSuccess(request, id, order_type):
    if request.user.is_authenticated:
        print(id)
        try:
            subscription_id = stripe.checkout.Session.retrieve(id)
            address = Address.objects.get(user=request.user)
            delivery = Delivery.objects.filter(sub_id=id).first()
        except:
            return HttpResponse('Invalid ID')
        context = {
            'payment_type': subscription_id.payment_method_types[0],
            'bank':'bank',
            'phone':address.contact,
            'name':address.fname + ' ' + address.lname,
            'email':subscription_id.customer_details.email,
            'product':delivery.product.product_name,
            'quantity':delivery.quantity,
            'amount': subscription_id.amount_total / 100,
            'id':id,
            'order_type':order_type,
        }
        return render(request, 'new_template/payment-sucessful.html', context)
    else:
        return HttpResponse('Invalid User')
