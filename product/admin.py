from django.contrib import admin
from django.db import models
from .models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    models = Category
    list_display = ["pk","name","gender","sport_type","color"]


class ProductAdmin(admin.ModelAdmin):
    models = Product
    list_display = ["pk","name","price","category","description","image"]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
