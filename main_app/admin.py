from django.contrib import admin
from .models import Itinerary, Attraction, Review

# Register your models here.
admin.site.register(Itinerary)
admin.site.register(Attraction)
admin.site.register(Review)
