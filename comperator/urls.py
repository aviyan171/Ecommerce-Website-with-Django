from unicodedata import name

from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()

router.register(r'productsview',views.ProductViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path('',views.index,name='index')
   
]