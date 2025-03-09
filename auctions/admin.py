from django.contrib import admin
from django.contrib.auth.models import User
from .models import Listing, Category, Bid, Comment

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'is_active', 'watching_users')  
    filter_horizontal = ('watching',)  
    def watching_users(self, obj):
        return ", ".join([user.username for user in obj.watching.all()])
    
    watching_users.short_description = "Watching Users"

# Register your models here.
admin.site.register(User)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Category)
admin.site.register(Bid)
admin.site.register(Comment)