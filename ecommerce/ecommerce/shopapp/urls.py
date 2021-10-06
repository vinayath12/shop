from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from  .import views
from django.urls import path, include
app_name='shopapp'
urlpatterns = [

    path('',views.allproduct,name='allproduct'),
    path('<slug:c_slug>/',views.allproduct,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='proDetail')
]