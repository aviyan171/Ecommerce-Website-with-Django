from dataclasses import field
from rest_framework import serializers
from ElectronicStore.models import Product

class ProductSerializer(serializers.ModelSerializer):
     class Meta:
         model=Product
         fields=('Product_Name','Category','brand','Price','Description','Specifications','Image')