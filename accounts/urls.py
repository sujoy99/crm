from django.urls import path
from .views import(
    home_view,
    product_view,
    customer_view
)

app_name="crm"
urlpatterns = [
    path('', home_view, name="home"),
    path('products/', product_view, name="products"),
    path('customer/<str:id>/', customer_view, name="customer"),
]