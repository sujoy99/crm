from django.urls import path
from .views import(
    home_view,
    product_view,
    customer_view,
    create_order_view,
    update_order_view,
    delete_order_view,
    registration_view,
    login_view,
    logout_view

)

app_name="crm"
urlpatterns = [
    path('register/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('', home_view, name="home"),
    path('products/', product_view, name="products"),
    path('customer/<int:id>/', customer_view, name="customer"),


    path('create-order/<int:id>/', create_order_view, name="create-order"),
    path('update-order/<int:id>/', update_order_view, name="update-order"),
    path('delete-order/<int:id>/', delete_order_view, name="delete-order"),
    
]