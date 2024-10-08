from django.shortcuts import render, redirect, get_object_or_404
from shoppingApp.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def _cart_Id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cartId=_cart_Id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cartId=_cart_Id(request))
        cart.save()
    try:
        cart_item = CartItem.objects.get(product = product_id, cart =cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
        cart_item.save()
    return redirect('cartApp:cart_detail')


def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cartId=_cart_Id(request))
        cart_items = CartItem.objects.filter(cart=cart,active=True)
        for item in cart_items:
            total += (item.product.price * item.quantity)
            counter += item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', dict(total=total, counter=counter, items=cart_items))


def remove_cart(request, product_id):
    cart = Cart.objects.get(cartId=_cart_Id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cartApp:cart_detail')


def delete(request, product_id):
    cart = Cart.objects.get(cartId=_cart_Id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cartApp:cart_detail')
