from django.db import models
from django.db.models.base import Model
from product.models import Product
from product.models import Category
from users.models import Customer


# Create your models here.



class Order(models.Model):
    PADDING = 'P'
    OUT_FOR_DELIVERY = 'OFD'
    DELIVERED = 'D'
    order_Status = [
        (PADDING, 'Padding'),
        (OUT_FOR_DELIVERY, 'Out For Delivery'),
        (DELIVERED, 'Delivered'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=200,blank=False, null=False )
    phone = models.CharField(max_length=13)
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=13,choices=order_Status,default='P')

    def __str__(self) -> str:
        return self.product.name

    def save(self, *args, **kwargs):
        if self.product is not None:
            self.price = self.product.price
        super().save(*args, **kwargs)
