from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Products(models.Model):
    Name=models.CharField(max_length=100)
    Quantity=models.IntegerField()
    Price=models.IntegerField()

    def __str__(self):
        return self.Name


