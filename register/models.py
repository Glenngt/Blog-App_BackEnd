from django.db import models

# Create your models here.

class RegisterModel(models.Model):
    name = models.CharField(default="",max_length=200)
    pic = models.CharField(default="",max_length=500)
    email = models.CharField(default="",max_length=300)
    pswd = models.CharField(default="",max_length=100)
