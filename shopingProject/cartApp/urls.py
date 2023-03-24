from django.urls import path
from . import views
app_name = 'cartApp'
urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
    path('delete/<int:product_id>/', views.delete, name='deleteCart')
]