from django import template

import product
from orders.models import Order

register = template.Library()

@register.filter(name='total')
def total(quantity,price):
    return quantity*price
    