from django.db import models
from users.models import Users
# Create your models here.

class Delivery(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    wallet = models.IntegerField()
    orders_count = models.IntegerField(default=0)
    working_status = models.BooleanField(blank=True, null=True)



class Ask(models.Model):
    class Status(models.TextChoices):
        CASH = 'cash', 'cash'
        CART = 'cart', 'cart'
        BOTH = 'both', 'both'

    question_text = models.CharField(max_length=200)
    status = models.CharField(
        choices=Status.choices,
    )

class Delivery_wallet_log(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    amount_cash = models.IntegerField(default=0)
    amount_cart = models.IntegerField(default=0)
    type = models.ForeignKey(Ask, on_delete=models.CASCADE)
    is_take = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)



class Week_days(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Delivery_workdays(models.Model):
    delivery_id = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    work_time = models.DateField()
    week_days = models.ManyToManyField(Week_days, blank=True, null=True)



class Delivery_addresses(models.Model):
    delivery_id = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    address_name = models.TextField(max_length=500)
    langitude = models.CharField(max_length=255)


class Delivery_group(models.Model):
    delivery_id = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    group_id = models.IntegerField()
    group_name = models.CharField(max_length=255)


class Delivery_group_topic(models.Model):
    delivery_group = models.ForeignKey(Delivery_group, on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=255)
    message_id = models.IntegerField()
    topic_id = models.IntegerField()