from django.shortcuts import render
from django.http import HttpResponse
from matplotlib.style import context
from rest_framework import viewsets
from ElectronicStore.models import Product
from .serialization import ProductSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Product.objects.all();
    serializer_class= ProductSerializer


def index(request):
    product_list=Product.objects.all()
    # print(product_list)
    context={
        'product_list':product_list
    }
    return render(request,"comperator/comperator.html",context)
# Create your views here.
