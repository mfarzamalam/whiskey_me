from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save
import stripe

class Category(models.Model):
    name = models.CharField(max_length=30 ,null=False, blank=False, unique=True)

    def __str__(self):
        return f'{self.name}'



IS_SUBSCRIPTION = (
    ('yes', 'yes'),
    ('no', 'no'),
)


class Product(models.Model):
    product_name = models.CharField(max_length=100 ,null=False, blank=False)
    age = models.CharField(max_length=100 ,null=True, blank=True)
    type = models.CharField(max_length=100 ,null=True, blank=True)
    abv = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True) 
    picture = models.ImageField(null=True, 
                                      validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])], blank=True)     
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    date_posted = models.DateTimeField(auto_now=True)
    # is_subscription = models.CharField(choices=IS_SUBSCRIPTION, max_length=100)
    product_stripe_id = models.CharField(max_length=100, null=True, blank=True)
    product_price_is_subscribe_id   = models.CharField(max_length=100, null=True, blank=True)
    product_price_not_subscribe_id   = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.product_name}'


# run after every product save method call
def post_save_product(sender, instance, created, *args, **kwargs):

    product       = Product.objects.get(pk=instance.pk)
    product_name  = product.product_name
    product_price = int(product.price*100)
    product_price_id = product.product_price_is_subscribe_id
    product_id       = product.product_stripe_id

    # When new product is created, object of product and price is created.
    if product.product_stripe_id is None or product.product_stripe_id == '':
        print("if")
        new_product_stripe_id = stripe.Product.create(name=product.product_name, images=[product.picture, ])

        new_product_price_is_subscribe_id = stripe.Price.create(
                                unit_amount=product_price,
                                currency="GBP",
                                recurring={"interval": "month"},
                                product=new_product_stripe_id.id,
                            )

        new_product_price_not_subscribe_id = stripe.Price.create(
                                unit_amount=product_price,
                                currency="GBP",
                                # recurring={"interval": "month"},
                                product=new_product_stripe_id.id,
                            )

        product.product_stripe_id = new_product_stripe_id.id
        product.product_price_is_subscribe_id = new_product_price_is_subscribe_id.id
        product.product_price_not_subscribe_id = new_product_price_not_subscribe_id.id
        product.save()

    # if the product with stripe id is already created, else block run
    else:
        print("else")
        get_product_object = stripe.Product.retrieve(product_id)

        get_price_object = stripe.Price.retrieve(product_price_id)
        amount           = get_price_object.unit_amount


        # when price is changed, new object of price is created
        # we cannot update the prvious price as that will not work
        if product_price != amount:
            print("else / if -> amount")
            new_price_is_subscribe_id = stripe.Price.create(
                                unit_amount=product_price,
                                currency="GBP",
                                recurring={"interval": "month"},
                                product=product_id,
                            )

            new_price_not_subscribe_id = stripe.Price.create(
                                unit_amount=product_price,
                                currency="GBP",
                                product=product_id,
                            )

            product.product_price_is_subscribe_id = new_price_is_subscribe_id.id
            product.product_price_not_subscribe_id = new_price_not_subscribe_id.id
            product.save()


        # checking if the product name is same or changed, if changed then change this into stripe as well
        if product_name != get_product_object.name:
            print("else / if -> name")
            stripe.Product.modify(product_id, name=product_name)

            

post_save.connect(post_save_product, sender=Product)