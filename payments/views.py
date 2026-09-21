from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Products
from .models import Cart, CartItem, Order, OrderItem


def get_cart(user):
    cart, _ = Cart.objects.get_or_create(user=user)
    return cart


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    cart = get_cart(request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    messages.success(request, f'Added {product.name} to cart.')
    return redirect('cart')


@login_required
def cart_view(request):
    cart = get_cart(request.user)
    return render(request, 'cart/cart.html', {'cart': cart})


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    messages.success(request, 'Item removed.')
    return redirect('cart')


@login_required
def checkout(request):
    cart = get_cart(request.user)
    if not cart.items.exists():
        messages.error(request, 'Cart is empty.')
        return redirect('cart')

    if request.method == 'POST':
        order = Order.objects.create(user=request.user, total=cart.total())
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                product_name=item.product.name,
                price=item.product.price,
                quantity=item.quantity,
            )
        cart.items.all().delete()
        messages.success(request, f'Order #{order.id} placed!')
        return redirect('orders')

    return render(request, 'cart/checkout.html', {'cart': cart})


@login_required
def orders_view(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('items')
    return render(request, 'cart/orders.html', {'orders': orders})
