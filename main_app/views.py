from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Itinerary

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def itinerarys_index(request):
  itinerarys = Itinerary.objects.all()
  return render(request, 'itinerarys/index.html', {
    'itinerarys': itinerarys
  })

def itinerarys_detail(request, itinerary_id):
   itinerary = Itinerary.objects.get(id=itinerary_id)
   return render(request, 'itinerarys/detail.html', {
      'itinerary': itinerary
   })

class ItineraryCreate(CreateView):
   model = Itinerary
   fields = ['name', 'date_from', 'date_to', 'location', 'description']

class ItineraryUpdate(UpdateView):
   model = Itinerary
   fields = '__all__'

class ItineraryDelete(DeleteView):
   model = Itinerary
   success_url = '/itinerarys'