from django.contrib import admin
from .models import Order

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    models = Order
    list_display =['product','customer','quantity','price','address','phone','date']

admin.site.register(Order,OrderAdmin)