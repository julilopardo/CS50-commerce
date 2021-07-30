from django.contrib import admin
from .models import User, AuctionListing, Comment, Bid, Watchlist

class AuctionListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "creator", "startbid", "currentbid", "is_active", "buyer", "category", "url_image", "description", "creationdate")

# Register your models here.
admin.site.register(User)
admin.site.register(AuctionListing, AuctionListingAdmin)
admin.site.register(Comment)
admin.site.register(Bid)
admin.site.register(Watchlist)


