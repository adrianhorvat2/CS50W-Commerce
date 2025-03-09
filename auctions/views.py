from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Listing, Category, Bid, Comment
from decimal import Decimal

from .models import User


def index(request):

    listings = Listing.objects.all()

    return render(request, "auctions/index.html", {
        "listings": listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_listing(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        price = request.POST["price"]
        image = request.POST["image"]
        category_id = request.POST["category"]
        category = Category.objects.get(id=category_id)

        listing = Listing(title=title, description=description, price=price, created_by=request.user, category=category, image=image)
        listing.save()

        return HttpResponseRedirect(reverse("index"))
    
    categorys = Category.objects.all()

    return render(request, "auctions/create_listing.html", {
        "categories": categorys
    })

def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)

    return render(request, "auctions/listing.html", {
        "listing": listing
    })

def watchlist(request):
    if request.method == 'POST':
        listing_id = request.POST["listing_id"]
        listing = Listing.objects.get(id=listing_id)
        user = request.user

        if listing in user.watching.all():
            user.watching.remove(listing)
        else:
            user.watching.add(listing)

        return HttpResponseRedirect(reverse("listing", args=(listing_id,)))

    return render(request, "auctions/watchlist.html", {
        "listings": request.user.watching.all()
    })

def bid(request, listing_id):  
    if request.method == "POST":
        listing = Listing.objects.get(id=listing_id)
        user = request.user
        bid_amount = Decimal(request.POST["bid"])

        if bid_amount > listing.price:
            bid = Bid(amount=bid_amount, created_by=user, listing=listing)
            bid.save()
            listing.price = bid_amount
            listing.save()
            message = "Your bid was placed successfully!"
        else:
            message = "Your bid must be higher than the current price."

    return render(request, "auctions/listing.html", {
        "listing": listing,  
        "message": message  
    })