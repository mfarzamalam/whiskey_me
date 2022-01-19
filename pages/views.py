from os import stat
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import View
from django.views.generic.base import TemplateView
from stripe.api_resources import customer, subscription
from .models import Review
from product.models import Category, Product
from registration.models import CustomUser
from order.models import Delivery, Address
from django.utils import timezone
from .forms import ReviewForm, CustomerAddressForm
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
import stripe

from whiskey_me.stripe_key import SECRET_KEY
stripe.api_key = SECRET_KEY


# Create your views here.
# def home(request):
#     return render(request, "pages/home.html")


class HomeView(View):
    # b = "012345678910"       
    # a = "abracadabra"
    # print(a)
    # print(a[:5] + 'k' + a[6:])

    def get(self, request,  *args, **kwargs):
        # if request.user.is_superuser:
            # return redirect('pages:admin_panel')
        # else:
        return render(request,'new_template/index.html')


class NewDashboard(LoginRequiredMixin, View):
    login_url = "/login/"
    def get(self, request,  *args, **kwargs):
        product = Product.objects.all()
        # get_5cl = Category.objects.get(name='5cl')
        # get_70cl = Category.objects.get(name='70cl')

        # prd_5cl = Product.objects.filter(category=get_5cl)
        # prd_70cl = Product.objects.filter(category=get_70cl)
        # for i in prd_70cl:
        #     print(i.product_name)

        context = {
            'product': product,
            # 'product_1': prd_5cl,
            # 'product_2': prd_70cl,
        }
        return render(request,'new_template/dashboard/admin_dashboard.html',context)


class ShopView(View):
    def get(self, request,  *args, **kwargs):
        product = Product.objects.all()
        # get_5cl = Category.objects.get(name='5cl')
        # get_70cl = Category.objects.get(name='70cl')

        # prd_5cl = Product.objects.filter(category=get_5cl)
        # prd_70cl = Product.objects.filter(category=get_70cl)
        # for i in prd_70cl:
        #     print(i.product_name)

        context = {
            'product': product,
            # 'product_1': prd_5cl,
            # 'product_2': prd_70cl,
        }
        if request.user.is_superuser:
            return redirect('pages:admin_panel')
        else:
            return render(request,'new_template/shop.html',context)


class ProductPriceRange(View):
    def get(self, request, fromm, to, *args, **kwargs):
        product = Product.objects.filter(price__range=[fromm, to])

        context = {
            'product': product,
        }

        return render(request,'new_template/shop.html',context)


class ProductAgeRange(View):
    def get(self, request, fromm, to, *args, **kwargs):
        product = Product.objects.filter(age__range=[fromm, to])
        context = {
            'product': product,
        }

        return render(request,'new_template/shop.html',context)


class ProductBottleSize(View):
    def get(self, request, size, *args, **kwargs):
        category = Category.objects.get(name=size)
        product  = Product.objects.filter(category=category)
        context = {
            'product': product,
        }

        return render(request,'new_template/shop.html',context)



class SingleCategoryView(View):
    def get(self, request, category, *args, **kwargs):
        selected_cat = Category.objects.get(name=category)
        product = Product.objects.filter(category=selected_cat)
        context = {
            'product': product,
        }

        return render(request,'pages/category_product.html', context)



class AboutView(View):
    def get(self, request,  *args, **kwargs):
        
        return render(request,'pages/about.html')



class ContactView(View):
    def get(self, request,  *args, **kwargs):
        context ={
            'review_form':ReviewForm()
        }
        return render(request,'pages/contact.html',context=context)
    
    
    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:home')

        context = {
            'review_form': form,
            
        }
        return render(request, 'pages/contact.html', context=context)



class AdminPanelView(LoginRequiredMixin, View):
    login_url = "/register/"
    def get(self, request, status="", *args, **kwargs):
        if request.user.is_superuser:
            print(status)
            if status == "single":
                singlePayment = stripe.PaymentIntent.list()
                required_single_data = []
                for s in singlePayment:
                    print(s.status)
                    if s.description != "Subscription creation" and s.status == "succeeded":
                        single_item = {
                            'id': s.id,
                            'product': Product.objects.filter(product_stripe_id=s.metadata.product_id).first(),
                            'current_period_start': datetime.datetime.fromtimestamp(float(s.created)),
                            'amount': s.metadata.product_price,
                            'quantity': s.metadata.quantity,
                            'total': float(s.metadata.total),
                            'status': s.status,
                        }
                        required_single_data.append(single_item)

                context = {
                    'single': required_single_data,
                    'class_active': status,
                }      

                return render(request,'new_template/dashboard/admin_dashboard.html', context)


            elif status == "" or status == None:
                subscription = stripe.Subscription.list(status="all")
            else:
                subscription = stripe.Subscription.list(status=status)

            required_subscription_data = []
            for s in subscription:
                single_subscription_item = {
                    'user':CustomUser.objects.filter(stripe_id=s.customer).first(),
                    'interval': s.plan.interval,
                    'product': Product.objects.filter(product_stripe_id=s.plan.product).first(),
                    'current_period_start': datetime.datetime.fromtimestamp(float(s.current_period_start)),
                    'current_period_end': datetime.datetime.fromtimestamp(float(s.current_period_end)),
                    'amount': s.plan.amount/100,
                    'quantity': s.quantity,
                    'total': (s.plan.amount/100) * (s.quantity),
                    'status': s.status,
                }
                
                required_subscription_data.append(single_subscription_item)

            context = {
                'subscription': required_subscription_data,
                'class_active': status,
            }      

            return render(request,'new_template/dashboard/admin_dashboard.html', context)
        
        else:
            return HttpResponseRedirect(reverse('/'))



class ReviewPanelView(View):
    def get(self, request, id,  *args, **kwargs):
        get_review=Review.objects.get(id=id)
        context = {
            'get_review':get_review
        }

        return render(request,'pages/review.html',context=context)



class CustomerDashboard(LoginRequiredMixin ,View):
    def get(self, request, p_type, *args, **kwargs):
        user = CustomUser.objects.get(email=request.user)
        stripe_user_id = user.stripe_id

        if p_type == "subscription":
            pass
            subscription = stripe.Subscription.list(customer=stripe_user_id, status="all")

            required_subscription_data = []
            for s in subscription:
                single_subscription_item = {
                    'id': s.id,
                    'collection_method': s.collection_method, 
                    'interval': s.plan.interval,
                    'product': Product.objects.filter(product_stripe_id=s.plan.product).first(),
                    'current_period_start': datetime.datetime.fromtimestamp(float(s.current_period_start)),
                    'current_period_end': datetime.datetime.fromtimestamp(float(s.current_period_end)),
                    'amount': s.plan.amount/100,
                    'quantity': s.quantity,
                    'total': (s.plan.amount/100) * (s.quantity),
                    'status': s.status,
                    'delivery':Delivery.objects.filter(address=Address.objects.filter(user=request.user).first()).first(),

                }
                
                required_subscription_data.append(single_subscription_item)

            context = {
                'subscription': required_subscription_data,
                'single_item': "false",
            }

        else:
            singlePayment = stripe.PaymentIntent.list(customer=stripe_user_id)
            required_single_data = []
            for s in singlePayment:
                if s.description != "Subscription creation" and s.status == "succeeded":
                    single_item = {
                        'id': s.id,
                        'product': Product.objects.filter(product_stripe_id=s.metadata.product_id).first(),
                        'current_period_start': datetime.datetime.fromtimestamp(float(s.created)),
                        'amount': s.metadata.product_price,
                        'quantity': s.metadata.quantity,
                        'total': float(s.metadata.total),
                        'delivery':Delivery.objects.filter(address=Address.objects.filter(user=request.user).first()).first(),
                    }
                    required_single_data.append(single_item)

            context = {
                'single': required_single_data,
                'single_item': "true",
            }

        return render(request,'new_template/dashboard/customer_dashboard.html', context)



class CancelView(TemplateView):
    template_name = "pages/cancel.html"



class CustomerCanceledSubscription(LoginRequiredMixin, View):
    def get(self, request, sub, *args, **kwargs):
        stripe.Subscription.delete(sub)
        return HttpResponseRedirect('/dashboard/subscription/')


class TermsView(TemplateView):
    template_name = "new_template/terms.html"


class CustomerAddressView(LoginRequiredMixin,View):
    login_url = "/login/"
    def get(self, request, *args, **kwargs):
        address = Address.objects.filter(user=request.user).first()
        if address:
            form = CustomerAddressForm(instance=address)
            context = {
                'myaccount': "true",
                'form':form,
            }
        else:
            form = CustomerAddressForm()
            context = {
                'myaccount': "true",
                'form':form,
            }

        return render(request,'new_template/dashboard/customer_account.html', context)

    def post(self, request, *args, **kwargs):
        address = Address.objects.filter(user=request.user).first()
        form = CustomerAddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/account/address/')
        else:
            context = {
                'myaccount': "true",
                'form':form,
            }
            return render(request,'new_template/dashboard/customer_account.html', context)



class CheckoutSingleAddressView(LoginRequiredMixin, View):
    login_url = "/login/"
    def get(self, request, *args, **kwargs):
        product  = request.GET.get('product_id')
        quantity = request.GET.get('buy-now')

        address = Address.objects.filter(user=request.user).exists()
        if address:
            return HttpResponseRedirect(f'/Buy-Now/{product}/{quantity}')
        else:
            form = CustomerAddressForm()
            context = {
                'form': form,
                'product': product,
                'quantity': quantity,
            }
            return render(request,'new_template/dashboard/customer_account.html', context)

    def post(self, request, *args, **kwargs):
        product   = request.POST.get('product')
        quantity  = request.POST.get('quantity')

        address = Address.objects.filter(user=request.user).first()
        form = CustomerAddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/Buy-Now/{product}/{quantity}')
        else:
            context = {
                'myaccount': "true",
                'form':form,
            }
            return render(request,'new_template/dashboard/customer_account.html', context)



class CheckoutMonthlyAddressView(LoginRequiredMixin, View):
    login_url = "/login/"
    def get(self, request, *args, **kwargs):
        product  = request.GET.get('product_id')
        quantity = request.GET.get('monthly')

        address = Address.objects.filter(user=request.user).exists()
        if address:
            return HttpResponseRedirect(f'/Monthly/{product}/{quantity}')
        else:
            form = CustomerAddressForm()
            context = {
                'form': form,
                'product': product,
                'quantity': quantity,
            }
            return render(request,'new_template/dashboard/customer_account.html', context)

    def post(self, request, *args, **kwargs):
        product  = request.POST.get('product')
        quantity = request.POST.get('quantity')

        address = Address.objects.filter(user=request.user).first()
        form = CustomerAddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/Monthly/{product}/{quantity}')
        else:
            context = {
                'myaccount': "true",
                'form':form,
            }
            return render(request,'new_template/dashboard/customer_account.html', context)