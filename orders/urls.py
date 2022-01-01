from django.contrib import admin
from django.urls import path
from .views import chack_out


app_name = 'orders'
urlpatterns = [
    path('chack_out/', chack_out, name='chack_out'),
   
]