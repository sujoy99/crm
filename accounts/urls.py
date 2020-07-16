from django.urls import path
from .views import(
    home_view,
    product_view,
    customer_view
)

urlpatterns = [
    path('', home_view),
    path('products/', product_view),
    path('customer/', customer_view),
]