from django.forms import ModelForm
from .models import Order
from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class OrderStateForm(ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'orderstates', 'important']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)