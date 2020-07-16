from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home_view(request):
    template_name = "accounts/dashboard.html"
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_order = orders.count()
    delivered = Order.objects.filter(status='Delivered').count() 
    pending = Order.objects.filter(status='Pending').count() 
    context = {
        'customers' : customers,
        'orders' : orders,
        'total_order' : total_order,
        'delivered' : delivered,
        'pending' : pending
    }
    return render(request, template_name, context)

def product_view(request):
    template_name = "accounts/products.html"
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, template_name, context)
def customer_view(request, id):
    template_name = "accounts/customer.html"
    customer = Customer.objects.get(id=id)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {
        'customer' : customer,
        'orders' : orders,
        'order_count' : order_count
    }
    return render(request, template_name, context)

