from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import product_Details,CheckoutView,payment,khaltiRequestView,khaltiverifyView

urlpatterns = [
    path('', views.store,name="Store"),
    path('productdetails/<int:pk>',views.product_Details.as_view(),name='productdetails'),
    path('cart/',views.Cart,name="cart"),
    path('pluscart/',views.increase_cart),
    path('minuscart/',views.decrease_cart),
    path('removecart/',views.remove_cart),
    path('show-cart/',views.show_cart,name="show-cart"),
    path('checkout/',CheckoutView.as_view(),name="checkout"), 
    path('paymentdone/',views.payment,name="paymentdone"),
    path('paymentcomplete/',views.paymentcomplete,name="paymentcomplete"),
    path('orders/',views.orders,name="orders"),
    path('khalti_request/',khaltiRequestView.as_view(),name="khalti_request"),
    path('khalti_verify/',khaltiverifyView.as_view(),name="khalti_verify"),
    path('ReviewProduct/',views.Review,name="Review"), 
    path('feedback/',views.feedback,name="contact"), 
    path('mobile/',views.Mobile,name="mobile"),
    path('save_review/<int:pid>',views.save_review,name="save_review"),
    path('mobile/<slug:data>',views.Mobile,name="mobiledata"),
    path('laptop/',views.laptop,name="laptop"),
    path('laptop/<slug:data>',views.laptop,name="laptopdata"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)