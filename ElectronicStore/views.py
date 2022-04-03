from ast import Add, Del
from audioop import add
from itertools import product
from os import stat
import re
from urllib import request
import zoneinfo
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views import View
from matplotlib import use
from .models import *
from math import ceil
from .models import Cart as model_cart
from django.db.models import Q
from django.http import JsonResponse
from .forms import CheckoutForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
# Create your views here.
def store(request):
    Mobiles=Product.objects.filter(Category="M")
    Laptop=Product.objects.filter(Category="L")
    # mobilelen= len(Mobiles)
    # Laptoplen=len(Laptop)
    # n=(mobilelen+Laptoplen)
    # nSlides= n//4 + ceil((n/4) + (n//4))
    params={'Mobile': Mobiles, 'Laptops':Laptop}
    return render(request,'store/store.html',params)

class product_Details(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,'store/productdetails.html',{'Product':product})




def Cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    print(user)
    print(product_id)
    print(product)
    model_cart(user=user,product=product).save()
    return redirect('/show-cart')

def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=model_cart.objects.filter(user=user)
        # print(cart)
        amount=0
       
        total_price=0.0
        cart_product=[p for p in model_cart.objects.all() if p.user==user ]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                tamount=(p.quantity * p.product.Price)
                shippingandvat=13/100*tamount+100
                # print(shippingandvat)
                amount+=tamount
                total_price=amount+shippingandvat
                print(total_price)
            return render(request,'store/Cart.html',{'carts':cart,'totalprice':total_price,'amount':amount})
        else:
            return render(request,'store/emptycart.html')
 

def increase_cart(request):
   if request.method == 'GET':
        # user=request.user
        prod_id=request.GET['prod_id']
        # print(prod_id)
        c=model_cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount=0
        cart_product=[p for p in model_cart.objects.all() if p.user==request.user ]
        for p in cart_product:
                tamount=(p.quantity * p.product.Price)
                shippingandvat=13/100*tamount+100
                amount+=tamount
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalprice':amount+shippingandvat,
            }
        return JsonResponse(data)

def decrease_cart(request):
   if request.method == 'GET':
        # user=request.user
        prod_id=request.GET['prod_id']
        c=model_cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount=0
        cart_product=[p for p in model_cart.objects.all() if p.user==request.user ]
        for p in cart_product:
                tamount=(p.quantity * p.product.Price)
                shippingandvat=13/100*tamount+100
                amount+=tamount
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalprice':amount+shippingandvat,
            }
        return JsonResponse(data)

def remove_cart(request):
   if request.method == 'GET':
        # user=request.user
        prod_id=request.GET['prod_id']
        c=model_cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount=0
        shippingandvat=0
        cart_product=[p for p in model_cart.objects.all() if p.user==request.user ]
        for p in cart_product:
                tamount=(p.quantity * p.product.Price)
                amount+=tamount
                shippingandvat=13/100*tamount+100
        data={
            'amount':amount,
            'totalprice':amount+shippingandvat,
             }
        return JsonResponse(data)
    

def Review(request):
    user=request.user
    # print(address)
    cart_items=model_cart.objects.filter(user=user)
    # print(cart_items)
    amount=0.0
    shippingandvat=0
    cart_product=[p for p in model_cart.objects.all() if p.user==request.user ]
    if cart_product:
        for p in cart_product:
            tamount=(p.quantity * p.product.Price)
            shippingandvat=13/100*tamount+100
            amount+=tamount
            total_price=amount+shippingandvat
        return render(request,'store/Review.html',{'totalprice':total_price,'cart':cart_items})

class CheckoutView(View):
    def get(self,*args,**kwargs):
        form=CheckoutForm()
        context={
            'form':form
        }
        return render(self.request,"store/Checkout.html",context)

    def post(self,*args,**kwargs):
        form=CheckoutForm(self.request.POST or None)
        if form.is_valid():
                Name=form.cleaned_data.get('Name')
                Email=form.cleaned_data.get('Email')
                # Address=form.cleaned_data.get('Address')
                # print(Address)
                City=form.cleaned_data.get('City')
                print(City)
                State=form.cleaned_data.get('State')
                # Zip_code=form.cleaned_data.get('Zip_code')
                # print(Zip_code)
                Phone_Number=form.cleaned_data.get('Phone_Number')
                # print(phonenumber)
                billing_Address=Delivery_Address(
                user=self.request.user,Name=Name,Email=Email,City=City,
                State=State,Phone_Number=Phone_Number
                )
                
                billing_Address.save()
        return redirect('/paymentdone')
      
     


def Mobile(request,data=None):
    if data==None:
        mobile=Product.objects.filter(Category="M")
    elif data=="Samsung" or data=="AGM" or data=="Sony" or data=="Tracphone" or data=="Google" or data=="Apple" or data=="Nokia" or data=="Oneplus" or data=="Motorola":
        mobile=Product.objects.filter(Category="M").filter(brand=data)
    elif data=='below':
        mobile=Product.objects.filter(Category="M").filter(Price__lte=100000,Price__gt=50000)
    elif data=='above':
        mobile=Product.objects.filter(Category="M").filter(Price__gt=100000)
    elif data=='below40000':
        mobile=Product.objects.filter(Category="M").filter(Price__lte=30000)

    return render(request,'store/mobile.html',{"Mobile":mobile})

def laptop(request,data=None):
    if data==None:
        laptop=Product.objects.filter(Category="L")
    elif data=="Acer" or data=="HP" or data=="ASUS" or data=="Apple" or data=="Alienware" or data=="MSI" or data=="Microsoft" or data=="Toshiba":
        laptop=Product.objects.filter(Category="L").filter(brand=data)
    elif data=='below':
        laptop=Product.objects.filter(Category="L").filter(Price__lte=100000,Price__gt=50000)
    elif data=='above':
        laptop=Product.objects.filter(Category="L").filter(Price__gt=100000)
    elif data=='below40000':
        laptop=Product.objects.filter(Category="L").filter(Price__lt=50000,Price__lte=60000)
    return render(request,'store/laptop.html',{"Laptop":laptop})

def payment(request):
    user=request.user
    address=Delivery_Address.objects.filter(user=user)
    print(address)
    Customer_details=Customer.objects.filter(user=user)
    print(Customer_details)
    
    # print(address)
    cart_items=model_cart.objects.filter(user=user)
    print(cart_items)
    amount=0.0
    shippingandvat=0
    cart_product=[p for p in model_cart.objects.all() if p.user==request.user ]
    if cart_product:
        for p in cart_product:
            tamount=(p.quantity * p.product.Price)
            shippingandvat=13/100*tamount+100
            amount+=tamount
            total_price=amount+shippingandvat
    return render(request,'store/payment.html',{'totalprice':total_price,'cart':cart_items,'address':address})
    
def paymentcomplete(request):
    user=request.user
    # custid=request.GET.get('custid')
    # Delivery_Addresss=Delivery_Address.objects.get(id=custid)
    Billing_address=Delivery_Address.objects.filter(user=user)
    # print(custid)
    # print(Delivery_Addresss)
    cart=model_cart.objects.filter(user=user)
    for c in cart:
        Order_Update(Customer_Name=user, user=user,product=c.product,quantity=c.quantity).save()
        c.delete()
    return redirect("orders")

def orders(request):
    return render(request,'orders.html')

def feedback(request):
    if request.method=="POST":
        
        Name=request.POST.get('Name','')
        Email=request.POST.get('Email','')
        Phone=request.POST.get('Phone','')
        Feedback=request.POST.get('Feedback','')
        contact=Contact(Name=Name,Email=Email,Phone=Phone,Feedback=Feedback)
        contact.save()
    return render(request,'store/contact.html')
