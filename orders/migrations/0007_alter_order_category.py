# Generated by Django 4.0 on 2021-12-24 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_product_category'),
        ('orders', '0006_alter_order_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='category',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
    ]
