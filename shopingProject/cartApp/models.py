from django.db import models
from shoppingApp.models import Product
# Create your models here.


class Cart(models.Model):
    cartId = models.CharField(max_length=250, blank=True)
    dateAdded = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['dateAdded']

    def __str__(self):
        return self.cartId


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product

