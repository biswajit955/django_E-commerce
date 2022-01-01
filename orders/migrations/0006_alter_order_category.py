# Generated by Django 4.0 on 2021-12-24 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_category_color_category_gender_category_sport_type_and_more'),
        ('orders', '0005_order_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
    ]
