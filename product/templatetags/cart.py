from django import template

import product

register = template.Library()


@register.filter(name='product_in_cart')
def product_in_cart(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False

@register.filter(name='product_quantity')
def product_quantity(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)

@register.filter(name='total_prize')
def total_prize(product,cart):
    total = product_quantity(product,cart)*product.price
    return total

@register.filter(name='total_cart_price')
def total_cart_price(products , cart):
    sum = 0
    for p in products:
        sum += total_prize(p , cart)

    return sum

@register.filter(name='no_of_product_in_cart')
def no_of_product_in_cart( cart):
    productid = cart.keys()
    productlen = len(productid)
    return productlen