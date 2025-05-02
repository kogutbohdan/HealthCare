from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from pages.tasks_model import*
from pages.shop_model import*
from django.dispatch import receiver
from django.db.models.signals import post_save

class MyUser(AbstractUser):
    weight = models.DecimalField(max_digits=6,decimal_places=3,default=0)
    height = models.DecimalField(max_digits=6,decimal_places=3,default=0)
    aime=models.TextField(max_length=100,default="")
    many=models.IntegerField(default=0)
    rating=models.IntegerField(default=0)
    points=models.IntegerField(default=0)
    things=models.ManyToManyField(ShopModel,blank=True)
    tasks=models.ManyToManyField(Tasks,blank=True)
    icon=models.ImageField(upload_to="icons/",default="icons/1b8908034c17b1ed4318a4d6c421369c646dabb9.png")
    def statistics_list(self):
        return self.statistics_set.all()
    
@receiver(post_save, sender=MyUser)
def add_all_tasks(sender, instance, created, **kwargs):
    if created:
        all_tasks = Tasks.objects.all()
        instance.tasks.set(all_tasks)

admin.site.register(MyUser)
    