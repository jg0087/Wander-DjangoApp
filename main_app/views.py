from django.shortcuts import render
from .models import Itinerary

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def itineraries_index(request):
  itineraries = Itinerary.objects.all()
  return render(request, 'itineraries/index.html', {
    'itineraries': itineraries
  })