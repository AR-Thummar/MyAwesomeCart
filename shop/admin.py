from django.contrib import admin

# Register your models here.
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id','product_name','category','price')


admin.site.register(Product,ProductAdmin)