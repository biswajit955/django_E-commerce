from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Category, Product
from django.contrib.sessions.models import Session
from django.db.models import Q
from users.models import Customer
from django.contrib import messages

def add_cart(request,productid,remove,add):
    # create a "cart" session variabel
    cart = request.session.get('cart')
    # if user have cart than go to cart
    if cart:
        # fetch quantity from "cart" dictionary usin "cart" key(productid)
        quntety = cart.get(productid)
        if quntety:
            if remove:
                cart[productid] = quntety-1
            elif add:
                cart[productid] = quntety+1
        else:
            # normal return
            cart[productid] = 1
    # if "cart" is empty than it's set null value("{}") and add 1 qunatity
    else:
        cart = {}
        cart[productid] = 1
    # all product and quantity add in cart distnairy
    request.session['cart'] = cart
    # if atomaticly create "null" key in cart than it's for delete "null" key from cart distnairy
    cart = removenull(cart)


def removenull(cart):
    for i in list(cart.keys()):
        print(i)
        if 'null'==i or 'None'==i:
            del cart['null']
    return cart


def home(request):
    # _____________home_______________
    category = Category.objects.all()
    categoryid = request.GET.get('categoryid')
    print(categoryid)
    if categoryid:
        product = Product.objects.filter(category=categoryid)
        print(product,"product")
    else:
        product = Product.objects.all()
    print("___________________")
    print(cart, "cart")
    data = {
        "categorys": category,
        "products": product,
    }
    return render(request, 'product/index.html', data)


def search(request):
    if request.method == 'GET':
        query = request.GET.get('a')
        # category = Category.objects.all()
        submitbutton = request.GET.get('submit')
        if query is not None:
            productid = request.POST.get('product')
            remove = request.POST.get('remove')
            add = request.POST.get('add')
            add_cart(request,productid,remove,add)
            results = Product.objects.filter(Q(name__icontains=query))
            context = {'results': results,
                       'submitbutton': submitbutton}
            return render(request, 'product/search.html', context)
        else:
            none = "<h3>not found</h3>"
            return HttpResponse(none)
    else:
        return render(request, 'product/search.html')


def cart(request):
    cart = request.session.get('cart')
    productid = removenull(cart)
    if len(cart.keys()) == 0:
        messages.error(request, f"Now your cart is empty")
    print(productid)
    # if productid is '':
    #     del cart['']
    product = Product.objects.filter(id__in=productid)
    print(productid, "productid")

    data = {
        'products': product,
    }
    return render(request, 'product/cart.html', data)


def product_details(request,id):
    product = Product.objects.get(id = id)
    # ________________cart__________________
    # get product id from html page
    productid = request.POST.get('product')
    remove = request.POST.get('remove')
    add = request.POST.get('add')
    add_cart(request,productid,remove,add)
    return render(request,'product/product_details.html',{'product': product})

def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount

    url for this function should be <str:id> not <int:id>
    - otherwise you need to add str() method for each dict representation.
    """
    cart = request.session.get('cart')
    print(id)
    print(cart[id])
    # decreases the cart quantity until deletes from cart
    quantity = cart[id] - 1
    print("________________", quantity)
    if quantity > 0:
        cart[id] = quantity
    elif quantity == 0:
        cart.pop(id)
    else:
        cart.pop(id)
    request.session['cart'] = cart
    if not cart:  # if all products be deleted from cart return to destination page
        return redirect(reverse('cart'))
    return redirect(reverse('cart'))
