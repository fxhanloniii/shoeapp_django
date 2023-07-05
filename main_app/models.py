from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Shoe(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    size = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image_url = models.CharField(max_length=200, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name

