from django.db import models

# Create your models here.
class UserModel(models.Model):
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=100)
    email=models.EmailField()     #提供了EmailField