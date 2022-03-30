from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(Order_Update)
admin.site.register(Shipping_Address)
admin.site.register(Cart)


# Register your models here.
