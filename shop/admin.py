from django.contrib import admin
from shop.models import Product,Brand


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name','brand','price')
    search_fields = ['name']

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
