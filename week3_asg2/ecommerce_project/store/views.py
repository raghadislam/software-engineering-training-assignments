#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'store/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('product_list')
    return render(request, 'store/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')




#def cart(request):
 #   cart = request.session.get('cart', {})
 #   return render(request, 'store/cart.html', {'cart': cart})

from .models import Product

def cart(request):
    # Get the cart from the session
    cart = request.session.get('cart', {})

    # Fetch product details for items in the cart
    products_in_cart = []
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        products_in_cart.append({
            'product': product,
            'quantity': quantity
        })

    return render(request, 'store/cart.html', {'products_in_cart': products_in_cart})


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if product_id in cart:
        del cart[product_id]
    request.session['cart'] = cart
    return redirect('cart')














from .models import Order, OrderItem

def checkout(request):
    cart = request.session.get('cart', {})
    if request.method == 'POST':
        shipping_address = request.POST['shipping_address']
        total_price = 0
        order = Order.objects.create(
            user=request.user,
            shipping_address=shipping_address,
            total_price=0  # We calculate this later
        )
        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)
            total_price += product.price * quantity
            OrderItem.objects.create(order=order, product=product, quantity=quantity)
        order.total_price = total_price
        order.save()
        request.session['cart'] = {}  # Clear the cart
        return render(request, 'store/order_success.html', {'total_price': total_price, 'shipping_address': shipping_address})
    return render(request, 'store/checkout.html', {'cart': cart})









'''

def checkout(request):
    cart = request.session.get('cart', {})
    total_price = 0
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        total_price += product.price * quantity

    if request.method == 'POST':
        # Simulate payment and save the order
        order = Order.objects.create(
            user=request.user,
            total_price=total_price,
            shipping_address=request.POST['shipping_address']
        )
        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)
            OrderItem.objects.create(order=order, product=product, quantity=quantity)
        # Clear the cart
        request.session['cart'] = {}
        return redirect('order_success')

    return render(request, 'store/checkout.html', {'cart': cart, 'total_price': total_price})

'''
# from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

