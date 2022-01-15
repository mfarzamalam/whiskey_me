from django.urls import path
from product.views import SingleProductView, BuyNow, MonthlySubscription, FaqPageView
# , test, test2

app_name = "product"

urlpatterns = [
    path('single_product/<int:id>', SingleProductView.as_view(), name='single_product'),
    path('Buy-Now/<int:p>/<int:q>/', BuyNow.as_view(), name='buy-now'),
    path('Monthly/<int:p>/<int:q>/', MonthlySubscription.as_view(), name='monthly'),
    path('faq/', FaqPageView.as_view(), name='faq'),

    # path('test/', test, name='test'),
    # path('test2/<video_id>/', test2, name='test2'),
]