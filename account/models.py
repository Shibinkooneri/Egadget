from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    image=models.ImageField(upload_to="product_images")
    price=models.IntegerField()
    options=(
        ('Mobile Phones','Mobile Phones'),
        ('Tablet','Tablet'),
        ('Smart Watch','Smart Watch'),
        ('BTspeaker','BTspeaker'),
        ('Laptops','Laptops')
    )
    category=models.CharField(max_length=100,choices=options)
    

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=500,default='cart')
    quantity=models.IntegerField(null=True)

    @property
    def totalamnt(self):
        tot=self.product.price*self.quantity
        return tot

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    options=(
        ('Order Placed','Order Placed'),
        ('Shipped','Shipped'),
        ('Order Pending','Order Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled')
    )
    status=models.CharField(max_length=100,choices=options,default='Order Placed')
    phone=models.IntegerField()
    address=models.CharField(max_length=500)
    quantity=models.IntegerField(default=1)