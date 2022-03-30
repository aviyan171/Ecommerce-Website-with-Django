from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import product_Details

urlpatterns = [
    path('', views.store,name="Store"),
    path('productdetails/<int:pk>',views.product_Details.as_view(),name='productdetails'),
    path('cart/',views.Cart,name="cart"),
    path('pluscart/',views.increase_cart,name="increase_cart"),
    path('show-cart/',views.show_cart,name="show-cart"),
    path('main/',views.Mainn,name="Main"),
    path('checkout/',views.Checkout,name="Checkout"), 
    path('mobile/',views.Mobile,name="mobile"),
    path('mobile/<slug:data>',views.Mobile,name="mobiledata"),
    path('laptop/',views.laptop,name="laptop"),
    path('laptop/<slug:data>',views.laptop,name="laptopdata"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)