from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    weights = models.DecimalField(max_digits=5,decimal_places=3,default=0)
    height = models.DecimalField(max_digits=5,decimal_places=3,default=0)
    aime=models.TextField(max_length=100,default="")
    many=models.IntegerField(default=0)
    rank=models.IntegerField(default=0)
    