
from django import forms
class CheckoutForm(forms.Form):
    Phone_Number=forms.CharField()
    Name=forms.CharField()
    Email=forms.EmailField()
    # address=forms.CharField(widget=forms.TextInput(attrs={"name":"Address","id":"address"}))
    City=forms.CharField()
    State=forms.CharField()
    # Zip=forms.CharField(widget=forms.TextInput(attrs={"name":"Zip_code",'id':"Zip"}))
    # Phonenumber=forms.CharField(widget=forms.TextInput(attrs={"name":"phonenumber","id":"phonenumbrt"}))
    
