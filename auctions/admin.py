from django.contrib import admin
from django.contrib.auth.models import User
from .models import Listing, Category, Bid, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Category)
admin.site.register(Bid)
admin.site.register(Comment)