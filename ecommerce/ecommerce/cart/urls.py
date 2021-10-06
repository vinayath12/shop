from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .import views
app_name='cart'
urlpatterns = [
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),

    path('',views.cartdetail,name='cartdetail'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('fullremove/<int:product_id>/', views.full_remove, name='full_remove'),
]