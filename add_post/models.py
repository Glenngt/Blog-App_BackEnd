from django.db import models

# Create your models here.

class AddPostModel(models.Model):
    userid = models.CharField(default = "", max_length = 100)
    title = models.CharField(default = "", max_length = 500)
    msg = models.CharField(default = "", max_length = 800)
    