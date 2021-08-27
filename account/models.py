from django.db import models

# Create your models here.
class register(models.Model):
    firstname=models.CharField(max_length=250,unique=True)
    lastname=models.CharField(max_length=250,unique=True)
    username=models.CharField(max_length=250,unique=True)
    email=models.EmailField(max_length=250)
    password=models.CharField(max_length=250)