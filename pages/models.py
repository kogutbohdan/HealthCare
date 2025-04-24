from django.db import models
from django.contrib import admin

class ShopModel(models.Model):
    costs=models.IntegerField(default=0)
    image=models.ImageField(upload_to="icons/")

admin.site.register(ShopModel)
