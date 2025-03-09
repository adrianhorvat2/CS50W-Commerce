from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.TextField(max_length=64)

    def __str__(self):
        return f'{self.name}' 

class Listing(models.Model):
    title = models.TextField(max_length=64)
    description = models.TextField(max_length=512)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bid_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    image = models.URLField()
    watching = models.ManyToManyField(User, blank=True, related_name='watching')
    is_active = models.BooleanField(default=True)
    listing_winner = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True, related_name='listing_winner')

    def __str__(self):
        return f'{self.title} by {self.created_by}'

class Comment(models.Model):
    text = models.TextField(max_length=512)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(Listing, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.text} by {self.created_by} on {self.listing}'

class Bid(models.Model):
    amount = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(Listing, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.amount} by {self.created_by} on {self.listing}'