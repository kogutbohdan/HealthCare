from django.db import models
class ShopModel(models.Model):
    costs=models.IntegerField(default=0)
    image=models.ImageField(upload_to="icons/")