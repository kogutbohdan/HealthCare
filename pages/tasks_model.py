from django.db import models
class Tasks(models.Model):
    name=models.CharField(max_length=20,default="")
    text=models.TextField()
    image=models.ImageField(upload_to="img_for_task/")
    many=models.IntegerField(default=0)
    points=models.IntegerField(default=0)