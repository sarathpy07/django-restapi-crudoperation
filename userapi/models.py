from django.db import models

# Create your models here.
class userapi(models.Model):
    name= models.CharField(max_length=200)
    email = models.EmailField()
    adress = models.CharField(max_length=200)
    phone = models.IntegerField()