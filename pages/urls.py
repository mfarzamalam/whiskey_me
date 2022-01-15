from django.urls import path
from .views import (
    AdminPanelView, HomeView,AboutView,ContactView,ReviewPanelView, CustomerDashboard, CustomerCanceledSubscription, 
    SingleCategoryView, CancelView, ShopView, NewDashboard, ProductPriceRange, ProductAgeRange, ProductBottleSize, 
    TermsView, CustomerAddressView, CheckoutSingleAddressView, CheckoutMonthlyAddressView
)

app_name = "pages"


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/price/<int:fromm>/<int:to>/', ProductPriceRange.as_view(), name='price_range'),
    path('shop/age/<int:fromm>/<int:to>/', ProductAgeRange.as_view(), name='age_range'),
    path('shop/bottle/<str:size>', ProductBottleSize.as_view(), name='size_range'),
    path('about/', AboutView.as_view(), name='about'),
    path('new/', NewDashboard.as_view(), name='new_db'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('admin_panel/', AdminPanelView.as_view(), name='admin_panel'),
    path('admin_panel/<status>/', AdminPanelView.as_view(), name='admin_panel'),
    path('review_panel/<int:id>', ReviewPanelView.as_view(), name='review_panel'),
    path('dashboard/<p_type>/', CustomerDashboard.as_view(), name='customer_dashboard'),
    path('dashboard/canceled/<sub>/', CustomerCanceledSubscription.as_view(), name='cancel_subscription'),
    
    path('category/<slug:category>/', SingleCategoryView.as_view(), name='category'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('terms', TermsView.as_view(), name='terms'),

    path('account/address/', CustomerAddressView.as_view(), name='address'),
    path('checkout/single/address/', CheckoutSingleAddressView.as_view(), name='single_address'),
    path('checkout/monthly/address/', CheckoutMonthlyAddressView.as_view(), name='monthly_address'),

]