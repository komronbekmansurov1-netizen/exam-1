from django.db import models
from users.models import Users
# Create your models here.

class Celler(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField(500)
    langitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    wallet = models.IntegerField()
    total_get_products_count = models.IntegerField()
    stock = models.IntegerField()


class Celler_wallet_log(models.Model):
    celler = models.ForeignKey(Celler, on_delete=models.CASCADE)
    amount = models.CharField(max_length=255)
    is_take = models.IntegerField()


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=None)
    image = models.ImageField(upload_to='image/')


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    celler = models.ForeignKey(Celler, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    stock_in_werehouse = models.IntegerField()
    selling_price = models.IntegerField()
    input_price = models.IntegerField()
    is_kombo = models.BooleanField(default=None)

class kombo_products(models.Model):
    kombo_id = models.ForeignKey('self', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
