from django.urls import path
from .views import CustomerDeliver, changeStatus, CustomerAddressDetials, test, CreateDelivery, paymentSuccess


app_name = 'order'


urlpatterns = [
    path('deliver/all/', CustomerDeliver.as_view(), name='deliver'),
    path('deliver/<status>/', CustomerDeliver.as_view(), name='deliver'),
    path('deliver/address/<pk>/', CustomerAddressDetials.as_view(), name='address_details'),
    path('change_delivery/<pk>/', changeStatus.as_view(), name='deliver_done'),
    path('create/delivery/<id>/<pk>/<quan>/<order_type>/', CreateDelivery, name='create_delivery'),

    path('payment-successful/',paymentSuccess, name='payment-successful'),
    path('test/', test, name='test'),
]