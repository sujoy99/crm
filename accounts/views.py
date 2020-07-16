from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    template_name = "accounts/dashboard.html"
    return render(request, template_name)

def product_view(request):
    template_name = "accounts/products.html"
    return render(request, template_name)
def customer_view(request):
    template_name = "accounts/customer.html"
    return render(request, template_name)

