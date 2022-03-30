from itertools import product
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views import View
from .models import *
from math import ceil
from .models import Cart as model_cart
from django.db.models import Q
from django.http import JsonResponse
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
        print(cart)
        amount=0
       
        total_price=0.0
        cart_product=[p for p in model_cart.objects.all() if p.user==user ]
        print(cart_product)
        if cart_product:
            for p in cart_product:
                tamount=(p.quantity * p.product.Price)
                shippingandvat=13/100*tamount+100
                print(shippingandvat)
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
        c=model_cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount=0
        cart_product=[p for p in model_cart.objects.all() if p.user==request.user ]
        for p in cart_product:
                tamount=(p.quantity * p.product.Price)
                shippingandvat=13/100*tamount+100
                amount+=tamount
                total_price=amount+shippingandvat
        data={
              'quantity':c.quantity,
                    'amount':amount,
                    'totalprice':total_price,
                }
        return JsonResponse(data)
    

def Mainn(request):
    return render(request,'store/Main.html')

def Checkout(request):
    return render(request,'store/Checkout.html')

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

