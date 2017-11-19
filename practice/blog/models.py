from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=50000)
    author = models.CharField(max_length=50)