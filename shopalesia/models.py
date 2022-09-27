from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    date_created = models.DateTimeField()
    is_paid = models.BooleanField(default=False)

    class Meta:
        db_table = 'orders'
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ('user', 'date_created', 'is_paid')




class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'products'
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name', 'price', 'stock')



class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name', 'id')
