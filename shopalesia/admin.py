from django.contrib import admin

from .models import Category, Product, Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    empty_value_display = 'H/Y'
    list_display = ('user', 'product', 'date_created', 'is_paid')
    list_filter = ('user', 'product', 'date_created', 'is_paid')

# admin.site.register(Category)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = 'H/Y'
    list_display = ('category', 'name', 'price', 'stock')
    list_filter = ('category', 'name', 'price', 'stock')
    search_fields = ('name', 'price')
    search_help_text = 'введите категорию и продукт'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = 'H/Y'
    list_display = ('name', 'is_published', 'id')
    list_filter = ('name', 'is_published')
    search_fields = ('name', 'is_published')
    search_help_text = 'введите категорию'

# Register your models here.
