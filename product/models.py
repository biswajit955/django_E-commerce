from django.db import models
from PIL import Image

# Create your models here.


class Category(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    BOTH = 'B'
    Gender = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (BOTH, 'Both'),
    ]
    FOOTBALL = 'F'
    CRICKET = 'C'
    BOTH = 'B'
    Type = [
        (FOOTBALL, 'Football'),
        (CRICKET, 'Creket'),
        (BOTH, 'Both'),
    ]
    RED = 'R'
    BLACK = 'B'
    PINK = 'P'
    DEFAULT ='D'
    Color = [
        (RED, 'Red'),
        (BLACK, 'Black'),
        (PINK, 'Pink'),
        (DEFAULT,'Default')
    ]
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=Gender, default='B')
    sport_type = models.CharField(max_length=6, choices=Type, default='B')
    color = models.CharField(max_length=6, choices=Color,default='D')

    def __str__(self) -> str:
        return self.name 
    
    def __unicode__(self):
        return (self.name)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(
        max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    image2 = models.ImageField(upload_to='uploads/products/',blank=True, null=True)
    image3 = models.ImageField(upload_to='uploads/products/',blank=True, null=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height>300 or img.width > 400:
            img.thumbnail((500,500))
            img.save(self.image.path)
