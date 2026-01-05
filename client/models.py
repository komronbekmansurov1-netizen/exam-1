from django.db import models
from users.models import Users
from seller.models import Product
# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Lead_status(models.Model):
    name = models.CharField(max_length=100)
    status_id = models.IntegerField()

    def __str__(self):
        return self.name


class Client(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    orders_count = models.IntegerField()
    retums_products_count = models.IntegerField()
    tags = models.ManyToManyField(Tags, blank=True)
    lead_id = models.IntegerField()
    lead_status_id = models.ForeignKey(Lead_status, on_delete=models.CASCADE)
    trek_number = models.IntegerField()
    custom_number = models.IntegerField()
    from_where = models.CharField(max_length=100)


class Favourities(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class Cart(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()