from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("bid/<int:listing_id>", views.bid, name="bid"),
    path("close_auction/<int:listing_id>", views.close_auction, name="close_auction"),
    path("comment/<int:listing_id>", views.comment, name="comment"),
    path("categories", views.category, name="category"),
    path("category/<str:name>", views.filter_by_category, name="filter_by_category")
]
