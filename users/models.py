from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=13)
    email_id = models.EmailField()
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name
