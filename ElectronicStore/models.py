
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Customer_Name=models.CharField(max_length=100,null=True)
    Email=models.CharField(max_length=100)

    def __str__(self):
        return self.Customer_Name

CATEGORY_CHOICES=(
        ("M","Mobile"),
        ('L',"Laptop")
    )
class Product(models.Model):
    Product_Name=models.CharField(max_length=50)
    Category=models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    brand=models.CharField(max_length=50,default="")
    Price=models.IntegerField(default=0)
    Description=models.CharField(max_length=10000)
    Specifications=models.CharField(max_length=10000,null=True)
    Image=models.ImageField(upload_to="products",default="")

    def __str__(self):
        return  (self.Product_Name)


class Contact(models.Model):
    Name=models.CharField(max_length=500)
    Email=models.CharField(max_length=500, default="")
    Phone=models.IntegerField(default=10)
    Feedback=models.CharField(max_length=500,default="")

    def __str__(self):
        return self.Name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    # def __str__(self):
    #     return str(self.id)

class Order(models.Model):
    Date_added=models.DateTimeField(default=timezone.now())
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    # def __str__(self):
    #     return s(self.id)
        
STATUS=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On the Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)
 
class Order_Update(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    update_desc=models.CharField(max_length=60,choices=STATUS,default='pending')
    ordered_date=models.DateField(default=timezone.now())
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.update_desc[0:7] + "....."

class Shipping_Address(models.Model):
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Email=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    State=models.CharField(max_length=100)
    Zip_Code=models.CharField(max_length=100)

    def __str__(self):
        return self.Address



