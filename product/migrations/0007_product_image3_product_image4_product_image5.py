# Generated by Django 4.0 on 2022-03-29 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(null=True, upload_to='uploads/products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(null=True, upload_to='uploads/products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image5',
            field=models.ImageField(null=True, upload_to='uploads/products/'),
        ),
    ]