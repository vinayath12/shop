from django.contrib import admin

# Register your models here.
from .models import Category,Product


class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,categoryadmin)
class productadmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable = ['stock','price','available']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Product,productadmin)