from .models import Order
from django import forms

class OrderForm(forms.ModelForm):
    class Meta:
        models = Order
        fields = ['firsr_naem','last_name','phone','email','address_line1','address_line2','country','state','city','order_note']



#Hello