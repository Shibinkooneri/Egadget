# Generated by Django 4.2.4 on 2023-08-04 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='product_images')),
                ('price', models.IntegerField()),
                ('category', models.CharField(choices=[('Mobile Phones', 'Mobile Phones'), ('Tablet', 'Tablet'), ('Smart Watch', 'Smart Watch'), ('BTspeaker', 'BTspeaker'), ('Laptops', 'Laptops')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Order Placed', 'Order Placed'), ('Shipped', 'Shipped'), ('Order Pending', 'Order Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Order Placed', max_length=100)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=500)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(default='cart', max_length=500)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]