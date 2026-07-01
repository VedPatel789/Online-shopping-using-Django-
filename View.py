from django.shortcuts import render, redirect
from .models import Product
from .models import Order, Product
from django.contrib.auth.decorators import login_required

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


# ADD TO CART
def add_to_cart(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1

    request.session['cart'] = cart
    return redirect('home')


# VIEW CART
def cart(request):
    cart = request.session.get('cart', {})
    products = []

    total = 0

    for id, qty in cart.items():
        product = Product.objects.get(id=id)
        product.qty = qty
        product.total = product.price * qty
        total += product.total
        products.append(product)

    return render(request, 'cart.html', {'products': products, 'total': total})
@login_required
def checkout(request):
    cart = request.session.get('cart', {})

    for id, qty in cart.items():
        product = Product.objects.get(id=id)

        Order.objects.create(
            user=request.user,
            product=product.name,
            price=product.price,
            quantity=qty
        )

    request.session['cart'] = {}
    return render(request, 'checkout.html')