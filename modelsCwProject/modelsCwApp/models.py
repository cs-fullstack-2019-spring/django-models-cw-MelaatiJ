from django.db import models

# Create your models here.

#from django databasee import models
from django.db import models



# model1 that asks for name, breed, color , and gender
class Dog(models.Model):
   name = models.CharField(max_length=200)
   breed = models.CharField(max_length=100)
   color = models.CharField(max_length=100)
   gender = models.CharField(max_length=100)


# model 2 that asks for username, real name, acountnumber and balance
class Account(models.Model):
    username = models.CharField(max_length=100)
    realName = models.CharField(max_length=200)
    accountNumber = models.IntegerField()
    balance =models.IntegerField()
