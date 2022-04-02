from django.contrib import admin
from django.urls import path
from .views import home,search,cart,adjust_cart,product_details
from orders.views import my_orders

urlpatterns = [
    path('', home, name='home'),
    path('search/',search,name="search"),
    path('cart/',cart,name='cart'),
    path('adjust/<str:id>/',adjust_cart, name="adjust_cart"),
    path('my_orders/', my_orders, name='my_orders'),
    path('product_details/<int:id>',product_details, name='product_details')
]