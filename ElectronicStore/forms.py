
from dataclasses import field
from django import forms
from .models import Product_Review
from django.contrib.auth.models import User

PAYMENT_CHOICES=(
('Cash on delivery','Cash on delivery'),
('Khalti','khalti'),
)
class CheckoutForm(forms.Form):
    Phone_Number=forms.CharField()
    Name=forms.CharField()
    Email=forms.EmailField()
    # address=forms.CharField(widget=forms.TextInput(attrs={"name":"Address","id":"address"}))
    City=forms.CharField()
    State=forms.CharField()
    payment_option=forms.ChoiceField(widget=forms.RadioSelect,choices=PAYMENT_CHOICES)
    # Zip=forms.CharField(widget=forms.TextInput(attrs={"name":"Zip_code",'id':"Zip"}))
    # Phonenumber=forms.CharField(widget=forms.TextInput(attrs={"name":"phonenumber","id":"phonenumbrt"}))

class ReviewAdd(forms.ModelForm):
    class Meta:
        model=Product_Review
        fields=('review_text','review_rating')
