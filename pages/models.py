from django.db import models
from django.contrib import admin
from registretion.models import MyUser
from django.db import models
from .tasks_model import*
from .shop_model import*


class Statistics(models.Model):
    number=models.IntegerField(default=0)
    task=models.ForeignKey(Tasks,on_delete=models.CASCADE)
    user=models.ForeignKey(MyUser,null=True,blank=True,on_delete=models.CASCADE)
    counts=models.IntegerField(default=0)
    coins=models.IntegerField(default=0)
    points=models.IntegerField(default=0)

class DefaultIcons(models.Model):
    image=models.ImageField(upload_to="icons/")
    
admin.site.register(ShopModel)
admin.site.register(Tasks)
admin.site.register(Statistics)
admin.site.register(DefaultIcons)