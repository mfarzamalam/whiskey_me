from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.views.generic.base import TemplateView
from stripe.api_resources import customer, subscription
from pages.models import Review
from product.models import Category, Product
from registration.models import CustomUser
from order.models import Delivery
from django.utils import timezone
from pages.forms import ReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
import stripe

from whiskey_me.stripe_key import SECRET_KEY
stripe.api_key = SECRET_KEY


# Create your views here.
# def home(request):
#     return render(request, "pages/home.html")


class HomeView(View):
    def get(self, request,  *args, **kwargs):
        # if request.user.is_superuser:
            # return redirect('pages:admin_panel')
        # else:
        return render(request,'new_template/index.html')


class NewDashboard(View):
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
                print(len(singlePayment))
                required_single_data = []
                for s in singlePayment:
                    if s.description != "Subscription creation":
                        single_item = {
                            'id': s.id,
                            'product': Product.objects.filter(product_stripe_id=s.metadata.product_id).first(),
                            'current_period_start': datetime.datetime.fromtimestamp(float(s.created)),
                            'amount': s.metadata.product_price,
                            'quantity': s.metadata.quantity,
                            'total': float(s.metadata.total),
                            'address': s.metadata.address_1,
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
                    # 'product': Product.objects.filter(product_stripe_id=s.plan.product),
                    'current_period_start': datetime.datetime.fromtimestamp(float(s.current_period_start)),
                    'current_period_end': datetime.datetime.fromtimestamp(float(s.current_period_end)),
                    'amount': s.plan.amount/100,
                    'quantity': s.quantity,
                    'total': (s.plan.amount/100) * (s.quantity),
                    'status': s.status,
                    'address': s.metadata,
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
                if s.description != "Subscription creation":
                    single_item = {
                        'id': s.id,
                        'product': Product.objects.filter(product_stripe_id=s.metadata.product_id).first(),
                        'current_period_start': datetime.datetime.fromtimestamp(float(s.created)),
                        'amount': s.metadata.product_price,
                        'quantity': s.metadata.quantity,
                        'total': float(s.metadata.total),
                        'address': s.metadata.address_1,
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

        return HttpResponseRedirect('/dashboard')



class AddSubscriptionAddress(View):
    def get(self, request, id, pk, quan, *args, **kwargs):
        context = {
            'id': id,
            'pk': pk,
            'quan': quan,
            'subs': "true",
        }
        return render(request,'pages/customer_address.html', context)


    def post(self, request, *args, **kwargs):
        checkout_exists  = False

        name      = request.POST.get('name')
        country   = request.POST.get('country')
        address_1 = request.POST.get('address_1')
        address_2 = request.POST.get('address_2')
        city      = request.POST.get('city')
        state     = request.POST.get('state')
        contact   = request.POST.get('contact')
        sub_id    = request.POST.get('sub_id')
        prod_id   = request.POST.get('prod_id')
        prod_quan = request.POST.get('prod_quan')

        try:
            checkout = stripe.checkout.Session.retrieve(sub_id)
            checkout_exists = True
            print("Checkout exists? ", checkout_exists)

            if checkout_exists == True:
                sub_id = checkout.subscription
        except:
            print("Checkout exists? ", checkout_exists)

        stripe.Subscription.modify(sub_id, 
            metadata=
                {
                    "name": name, 
                    "country":country,
                    "address_1":address_1,
                    "address_2":address_2,
                    "city":city,
                    "state":state,
                    "city":city,
                },
        )
        Delivery.objects.create(
            user      = request.user,
            name      = name,
            country   = country,
            address_1 = address_1,
            address_2 = address_2,
            city      = city,
            state     = state,
            contact   = contact,
            sub_id    = sub_id,
            date      = timezone.now(),
            product   = Product.objects.get(pk=prod_id),
            quantity  = prod_quan,
        )
        return HttpResponseRedirect('/dashboard/subscription')



class AddSingleAddress(View):
    def get(self, request, id, pk, quan, *args, **kwargs):
        context = {
            'id': id,
            'pk': pk,
            'quan': quan,
            'subs': "false",
        }
        return render(request,'new_template/dashboard/address.html', context)


    def post(self, request, *args, **kwargs):
        checkout_exists  = False

        name      = request.POST.get('name')
        country   = request.POST.get('country')
        address_1 = request.POST.get('address_1')
        address_2 = request.POST.get('address_2')
        city      = request.POST.get('city')
        state     = request.POST.get('state')
        contact   = request.POST.get('contact')
        single_id = request.POST.get('single_id')
        prod_id   = request.POST.get('prod_id')
        prod_quan = request.POST.get('prod_quan')

        try:
            checkout = stripe.checkout.Session.retrieve(single_id)
            checkout_exists = True
            print("Checkout exists? ", checkout_exists)

            if checkout_exists == True:
                single_id = checkout.payment_intent
        except:
            print("Checkout exists? ", checkout_exists)
        

        stripe.PaymentIntent.modify(single_id, 
            metadata=
                {
                    "name": name, 
                    "country":country,
                    "address_1":address_1,
                    "address_2":address_2,
                    "city":city,
                    "state":state,
                    "city":city,
                },
        )
        Delivery.objects.create(
            user      = request.user,
            name      = name,
            country   = country,
            address_1 = address_1,
            address_2 = address_2,
            city      = city,
            state     = state,
            contact   = contact,
            sub_id    = single_id,
            date      = timezone.now(),
            product   = Product.objects.get(pk=prod_id),
            quantity  = prod_quan,
        )
        return HttpResponseRedirect('/dashboard/single')