# Generated by Django 4.0 on 2021-12-24 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_order_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='category',
        ),
    ]
