import googlemaps
from django.conf import settings
from .models import Attraction

def fetch_and_save_attractions(keyword, location):
    gmaps = googlemaps.Client(key=settings.GOOGLE_PLACES_API_KEY)
    attractions = gmaps.attractions(query=keyword, location=location)
    for attraction in attractions['results']:
        name = attraction['name']
        location = attraction['formatted_address']

        Attraction.objects.create(name=name, location=location)