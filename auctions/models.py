from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.TextField(max_length=64) 

class Listing(models.Model):
    title = models.TextField(max_length=64)
    description = models.TextField(max_length=512)
    price = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    image = models.URLField()

class Comment(models.Model):
    text = models.TextField(max_length=512)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(Listing, on_delete = models.CASCADE)

class Bid(models.Model):
    amount = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(Listing, on_delete = models.CASCADE)