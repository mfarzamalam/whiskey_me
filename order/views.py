from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import Delivery
import stripe


from whiskey_me.stripe_key import SECRET_KEY
stripe.api_key = SECRET_KEY


# Create your views here.


class CustomerDeliver(View):
    def get(self, request, status="", *args, **kwargs):
        if status == "" or status == None:
            items = Delivery.objects.all()
            class_active = None
            action = None
        else:
            items  = Delivery.objects.filter(delivery=status)
            action = status
            class_active = status
        
        
        context = {'items': items, 'class_active':class_active, 'action':action}
        return render(request, 'order/delivery.html', context)


class CustomerAddressDetials(View):
    def get(self, request, pk, *args, **kwargs):
        items  = Delivery.objects.get(pk=pk)
        context = {
            'item':items
        }

        return render(request, 'order/address_details.html', context)


class changeStatus(View):
    def post(self, request, pk, *args, **kwargs):
        status = request.POST.get('status')
        item = Delivery.objects.get(pk=pk)
        item.delivery = status
        item.save()

        return redirect('order:deliver')