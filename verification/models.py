from django.db import models


# Create your models here.

class UserVerification(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    code = models.CharField(max_length=6, default="-1")
    created_at = models.DateTimeField(auto_now_add=True)
