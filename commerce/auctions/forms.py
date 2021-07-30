from django import forms
from django.forms.models import ModelChoiceField
from .models import AuctionListing

class AuctionListingForm(forms.ModelForm):
    
    class Meta:
        model= AuctionListing
        fields= ["url_image"]
        labels = {"url_image" : "Upload a picture"}
