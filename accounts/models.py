from django.db import models
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=120, null=True)
    phone = models.CharField(max_length=120, null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("crm:customer", kwargs={'id':self.id})

class Tag(models.Model):
    name = models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATAGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor')
    )
    name = models.CharField(max_length=120, null=True)
    price = models.FloatField(null=True)
    catagory = models.CharField(max_length=120, null=True, choices=CATAGORY)
    description = models.CharField(max_length=220, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivary', 'Out for delivary'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL) 
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status =  models.CharField(max_length=120, null=True, choices=STATUS)
    