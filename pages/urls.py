from django.urls import path
from pages.views import (
    AdminPanelView, HomeView,AboutView,ContactView,ReviewPanelView, CustomerDashboard, CustomerCanceledSubscription, 
    AddSubscriptionAddress, AddSingleAddress, SingleCategoryView, CancelView, ShopView
)

app_name = "pages"


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    # path('', HomePageView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('admin_panel/', AdminPanelView.as_view(), name='admin_panel'),
    path('admin_panel/<status>/', AdminPanelView.as_view(), name='admin_panel'),
    path('review_panel/<int:id>', ReviewPanelView.as_view(), name='review_panel'),
    path('dashboard/<p_type>/', CustomerDashboard.as_view(), name='customer_dashboard'),
    path('dashboard/canceled/<sub>/', CustomerCanceledSubscription.as_view(), name='cancel_subscription'),
    path('address/subscribe/', AddSubscriptionAddress.as_view(), name='sub_address'),
    path('address/subscribe/<id>/<pk>/<quan>/', AddSubscriptionAddress.as_view(), name='sub_address'),

    path('address/single/', AddSingleAddress.as_view(), name='single_address'),
    path('address/single/<id>/<pk>/<quan>/', AddSingleAddress.as_view(), name='single_address'),

    path('category/<slug:category>/', SingleCategoryView.as_view(), name='category'),
    path('cancel/', CancelView.as_view(), name='cancel'),
]