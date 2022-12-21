from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=25)
    lastname=models.CharField(max_length=25, default="")
    email=models.EmailField(max_length=254, default="")
    password=models.CharField(max_length=254)
    
class Image(models.Model):
    categoryId=models.PositiveIntegerField()
    
class Category(models.Model):
    name=models.CharField(max_length=30)