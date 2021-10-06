from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from  .import views
from django.urls import path, include
app_name='searchapp'
urlpatterns = [

    path('',views.search,name='search'),
]