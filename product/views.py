from pipes import Template
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from .models import Product, Category
from registration.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
import stripe


from whiskey_me.stripe_key import SECRET_KEY
stripe.api_key = SECRET_KEY


# Create your views here.
class ProductPageView(TemplateView):
    template_name = "new_template/product-page.html"


class SingleProductView(View):
    def get(self, request, id , *args, **kwargs):
        get_product = Product.objects.filter(id=id).first()
        if get_product.category.name == '5cl':
            get_category = Category.objects.filter(name = '5cl').first()
            get_related =Product.objects.filter(category = get_category)
        if get_product.category.name == '70cl':
            get_category = Category.objects.filter(name = '70cl').first()
            get_related = Product.objects.filter(category = get_category)
        context = {
            'product': get_product, 
            'related': get_related
        }    
        return render(request,'new_template/product-page.html',context=context)   



class BuyNow(LoginRequiredMixin, View):
    login_url = "/login/"
    def get(self, request, p, q, *args, **kwargs):
        product  = p
        quantity = q

        get_product = Product.objects.filter(pk=product).first()
        stripe_not_subscribe_price_id = get_product.product_price_not_subscribe_id

        user = CustomUser.objects.filter(email=request.user).first()
        stripe_user_id = user.stripe_id

        
        LOCAL_DOMAIN = 'http://127.0.0.1:8000/'
        PYTHONANYWHERE_DOMAIN = 'http://whiskeymeee.pythonanywhere.com/'
        
        checkout_session = stripe.checkout.Session.create(
            
            customer = stripe_user_id,
            line_items=[
                {
                    'price': stripe_not_subscribe_price_id,
                    'quantity': quantity,
                    
                },
            ],
            payment_method_types=['card',],
            mode='payment',   # for one time payment
            
            payment_intent_data={
                'metadata':{
                        'product_id': get_product.product_stripe_id,
                        'product_price':get_product.price,
                        'quantity':quantity,
                        'total':int(get_product.price) * int(quantity),
                    },
            },

            success_url=LOCAL_DOMAIN + f"orders/create/delivery/{{CHECKOUT_SESSION_ID}}/{product}/{quantity}/single/",
            cancel_url=LOCAL_DOMAIN + f'single_product/{product}',
        )

        return redirect(checkout_session.url, code=303)



class MonthlySubscription(LoginRequiredMixin, View):
    login_url = "/login/"
    def get(self, request, p, q, *args, **kwargs):
        product  = p
        quantity = q
        
        get_product = Product.objects.filter(pk=product).first()
        stripe_is_subscribe_price_id = get_product.product_price_is_subscribe_id

        user = CustomUser.objects.filter(email=request.user).first()
        stripe_user_id = user.stripe_id

        # 4242 4242 4242 4242 -- Fake card to test the checkout session
        LOCAL_DOMAIN = 'http://127.0.0.1:8000/'
        PYTHONANYWHERE_DOMAIN = 'http://whiskeymeee.pythonanywhere.com/'

        checkout_session = stripe.checkout.Session.create(
            customer = stripe_user_id,
            line_items=[
                {
                    'price': stripe_is_subscribe_price_id,
                    'quantity': quantity,
                },
            ],
            payment_method_types=['card',],
            mode='subscription',
            success_url=LOCAL_DOMAIN + f"address/subscribe/{{CHECKOUT_SESSION_ID}}/{product}/{quantity}",
            cancel_url=LOCAL_DOMAIN + '/',
        )

        return redirect(checkout_session.url, code=303)



class FaqPageView(TemplateView):
    template_name = 'new_template/faq-contact.html'