from django.contrib import admin

from .models import Category, Product, Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    empty_value_display = 'H/Y'
    list_display = ('user', 'product', 'date_created', 'is_paid')

# admin.site.register(Category)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = 'H/Y'
    list_display = ('category', 'name', 'price', 'stock')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = 'H/Y'
    list_display = ('name', 'is_published', 'id')

# Register your models here.
