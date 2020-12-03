from django.urls import path

from .views import ShopListView, Cart, Checkout

urlpatterns = [
    path('', ShopListView.as_view(), name='shop_view_url'),
    path('cart/', Cart.as_view(), name='cart_url'),
    path('checkout/', Checkout.as_view(), name='checkout_url'),
]