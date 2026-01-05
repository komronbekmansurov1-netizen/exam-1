from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    class Role(models.TextChoices):
        super_name = 'super_name', 'super_admin'
        admin = 'admin', 'admin'
        delivery = 'delivery', 'delivery'
        merchant = 'merchant', 'merchant'
        client = 'client', 'client'
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    role = models.CharField(max_length=255, choices=Role.choices)
    address = models.TextField(max_length=500)
    email = models.CharField(max_length=100)
    telegram_id = models.IntegerField(max_length=100)
    step = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
