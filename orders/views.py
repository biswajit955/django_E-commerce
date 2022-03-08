from django.http import request
from django.shortcuts import redirect, render
from product.models import Category, Product
from .models import Order
from users.models import Customer
from django.contrib import messages


# Create your views here.


def removenull(cart):
    if 'null' in list(cart.keys()) or 'None' in list(cart.keys()):
        del cart['null']
    return cart


def chack_out(request):
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    customer = request.session.get('customer')
    cart = request.session.get('cart')
    print(list(cart.keys()))

    removenull(cart)

    print(list(cart.keys()),"cart_lenth")
    products = Product.objects.filter(id__in=list(cart.keys()))

    print(address, phone, customer, cart, products)

    for product in products:
        print(cart.get(str(product.id)))
        order = Order(customer=Customer(id=customer),
                      product=product,
                      price=product.price,
                      address=address,
                      phone=phone,
                      quantity=cart.get(str(product.id)))
        order.save()
    messages.success(request, f"Your orders is done")
    request.session['cart'] = {}

    return redirect('cart')


def my_orders(request):
    customer_id = request.session.get('customer')
    customer=Customer.objects.get(id=customer_id)
    orders = Order.objects.filter(customer=customer_id)

    data = {
        'order': orders,
        'customer':customer,
    }
    return render(request, 'orders.html', data)
