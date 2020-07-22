from django.urls import path
from django.contrib.auth import views as auth_views
from .views import(
    home_view,
    product_view,
    customer_view,
    user_view,
    account_settings_view,
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
    path('user/', user_view, name="user-page"),
    path('settings/', account_settings_view, name="account"),
    path('products/', product_view, name="products"),
    path('customer/<int:id>/', customer_view, name="customer"),


    path('create-order/<int:id>/', create_order_view, name="create-order"),
    path('update-order/<int:id>/', update_order_view, name="update-order"),
    path('delete-order/<int:id>/', delete_order_view, name="delete-order"),

    # path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="password_reset"),

    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
    
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),
    
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete"),

    # ---> add this in main url

    
]