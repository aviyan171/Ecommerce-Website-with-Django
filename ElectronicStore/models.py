
from operator import mod
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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

class Delivery_Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    # Products=models.ForeignKey(Product,on_delete=models.CASCADE)
    Phone_Number=models.CharField(max_length=10)
    Name = models.CharField(max_length=90)
    Email = models.CharField(max_length=111)
    # Address = models.CharField(max_length=111,null=True)
    City = models.CharField(max_length=111)
    State = models.CharField(max_length=111)
    # Zip_code = models.CharField(max_length=111,default=0,null=True,blank=True)
    # phonenumber = models.CharField(max_length=111, default=1,null=True,blank=True)

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Customer_Name=models.CharField(max_length=100,null=True)
    Cust_Address=models.ForeignKey(Delivery_Address,on_delete=models.CASCADE,default="")

    def __str__(self):
        return str(self.id)




class Contact(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    Name=models.CharField(max_length=500,default="")
    Email=models.CharField(max_length=500, default="")
    Phone=models.IntegerField(default=10)
    Feedback=models.CharField(max_length=500,default="")

    def __str__(self):
        return self.Feedback[0:15]

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
PAYMENYTMETHOD=(
    ('Cash on devliery','Cash on delivery'),
    ("Khalti","Khalti"),
    )

class Order_Update(models.Model):
    billing_address=models.ForeignKey(Delivery_Address,on_delete=models.SET_NULL,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Customer_Name=models.CharField(max_length=10,default="")
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    update_desc=models.CharField(max_length=60,choices=STATUS,default='pending')
    ordered_date=models.DateField(default=timezone.now())
    quantity=models.PositiveIntegerField(default=1)
    payment_method=models.CharField(max_length=20,choices=PAYMENYTMETHOD,default="Cash on Devliery")
    payment_complete=models.BooleanField(default=False,null=True)
    def __str__(self):
        return self.update_desc[0:7] + "....."

RATING=(
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5')
)

class Product_Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    review_text=models.TextField()
    review_rating=models.CharField(choices=RATING,max_length=150)






