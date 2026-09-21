from django.urls import path
from .views import add_to_cart, cart_view, remove_from_cart, checkout, orders_view

urlpatterns = [
    path('', cart_view, name='cart'),
    path('add/<int:product_id>/', add_to_cart, name='add-to-cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove-from-cart'),
    path('checkout/', checkout, name='checkout'),
    path('orders/', orders_view, name='orders'),
]
