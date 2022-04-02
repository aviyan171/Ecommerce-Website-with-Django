from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(Order_Update)
admin.site.register(Cart)
admin.site.register(Delivery_Address)

# Register your models here.
