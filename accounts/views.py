from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import *
from .filters import OrderFilter
from .forms import OrderForm, CreateUserForm, CustomerForm
from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.
@unauthenticated_user
def registration_view(request):
    template_name = "accounts/register.html"
    
    # not showing register & login page after login
    # if request.user.is_authenticated:
    #     return redirect('crm:home')
    # else:
    # using default usercreation form to create user
    form = CreateUserForm(request.POST or None)
    # form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()

        # to show username in his dashboard
        username = form.cleaned_data.get("username")

        # default assining in customer group 
        group = Group.objects.get(name='customer')
        user.groups.add(group)

        # assining into customer model registered user
        Customer.objects.create(user=user, name=user.username, email=user.email)
        # showing temporary flash message
        messages.success(request, "Account was created for " + username)
        return redirect('crm:login')
    context = {
        'form' : form
    }
    return render(request, template_name, context)

@unauthenticated_user
def login_view(request):
    template_name = "accounts/login.html"
   
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('crm:home')
        else:
            messages.info(request, "Username or Password was incorret")
    context = {}
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('crm:login')

@login_required(login_url='crm:login')
@allowed_users(allowed_roles=['customer'])
def user_view(request):
    template_name = "accounts/user.html"
    # print(request.user.customer.order_set.all())
    orders = request.user.customer.order_set.all()
    total_order = orders.count()
    delivered = orders.filter(status='Delivered').count() 
    pending = orders.filter(status='Pending').count() 
    context = {
        'orders' : orders,
        'total_order' : total_order,
        'delivered' : delivered,
        'pending' : pending
    }
    return render(request, template_name, context)

@login_required(login_url='crm:login')
@allowed_users(allowed_roles=['customer'])
def account_settings_view(request):
    template_name = "accounts/account_settings.html"
    
    # grab logged in user specific user
    customer = request.user.customer
    # print(customer)
    # request.FILES for file uploading
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

        

    context = {
        'form' : form
    }
    return render(request, template_name, context)

@login_required(login_url='crm:login')
# @allowed_users(allowed_roles=['admin'])
@admin_only
def home_view(request):
    template_name = "accounts/dashboard.html"
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_order = orders.count()
    delivered = orders.filter(status='Delivered').count() 
    pending = orders.filter(status='Pending').count() 
    context = {
        'customers' : customers,
        'orders' : orders,
        'total_order' : total_order,
        'delivered' : delivered,
        'pending' : pending
    }
    return render(request, template_name, context)

@login_required(login_url='crm:login')
@allowed_users(allowed_roles=['admin'])
@admin_only
def product_view(request):
    template_name = "accounts/products.html"
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, template_name, context)

@login_required(login_url='crm:login')
@allowed_users(allowed_roles=['admin'])
@admin_only
def customer_view(request, id):
    template_name = "accounts/customer.html"
    customer = Customer.objects.get(id=id)
    orders = customer.order_set.all()
    order_count = orders.count()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context = {
        'customer' : customer,
        'orders' : orders,
        'order_count' : order_count,
        'myFilter' : myFilter
    }
    return render(request, template_name, context)

@login_required(login_url='crm:login')
@allowed_users(allowed_roles=['admin'])
@admin_only
def create_order_view(request, id):
    template_name = "accounts/order-form.html"
    
    customer = Customer.objects.get(id=id)
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5)
    formset = OrderFormSet(instance=customer, queryset=Order.objects.none())
    # form = OrderForm(request.POST or None, initial={'customer':customer})
    if request.method == "POST":
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {
        'formset' : formset,
        'tag'  : "Create"
    }
    return render(request, template_name, context)

@login_required(login_url='crm:login')
@allowed_users(allowed_roles=['admin'])
@admin_only
def update_order_view(request, id):
    template_name = "accounts/order-form.html"
    item = Order.objects.get(id=id)
    form = OrderForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/')

    context = {
        'form' : form,
        'tag'  : "Update"
    }
    return render(request, template_name, context)

@login_required(login_url='crm:login')
@allowed_users(allowed_roles=['admin'])
@admin_only
def delete_order_view(request, id):
    template_name = "accounts/delete.html"
    item = Order.objects.get(id=id)
    
    if request.method == "POST":
        item.delete()
        return redirect('/')

    context = {
        'item' : item
    }
    return render(request, template_name, context)