from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class Orders(models.Model):
    Name=models.CharField(max_length=100)
    Order_Number=models.IntegerField()
    Quantity=models.IntegerField(default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags=TaggableManager()
    favourites=models.ManyToManyField(User,related_name='favourite',default=None,blank=None)

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})
