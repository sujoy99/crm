from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.conf import settings 
from .models import *

# User = settings.AUTH_USER_MODEL

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'email',
            'password1',
            'password2'
        ]