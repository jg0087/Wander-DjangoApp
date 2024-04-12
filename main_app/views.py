from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# importing models
from .models import Itinerary, Attraction, List
# importing forms
from .forms import ListForm, ReviewForm
from django.core.management.base import BaseCommand
from .utils import fetch_and_save_attractions
from django.http import JsonResponse
import requests
import os

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


# @login_required
# def itinerarys_user_index(request):
  # itinerarys = Itinerary.objects.filter(user=request.user)
  # return render(request, 'itinerarys/user/index.html', {
  #   'itinerarys': itinerarys
  # })

@login_required
def itinerarys_detail(request, itinerary_id):
   itinerary = Itinerary.objects.get(id=itinerary_id)
   list_form = ListForm()
   list = List.objects.all()
   print(itinerary)
   id_list = itinerary.attractions.all().values_list('id')
   attractions_itinerary_doesnt_have = Attraction.objects.exclude(id__in=id_list)
   return render(request, 'itinerarys/detail.html', {
      'itinerary': itinerary,
      'list_form': list_form,
      'list': list,
      'attractions_itinerary_doesnt_have': attractions_itinerary_doesnt_have
   })

class ItineraryCreate(LoginRequiredMixin, CreateView):
   model = Itinerary
   fields = ['name', 'date_from', 'date_to', 'location', 'description']
   
   def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class ItineraryUpdate(LoginRequiredMixin, UpdateView):
   model = Itinerary
   fields = ['name', 'date_from', 'date_to', 'location', 'description']


class ItineraryDelete(LoginRequiredMixin, DeleteView):
   model = Itinerary
   success_url = '/itinerarys'

  

# class AttractionList(ListView):
#   model = Attraction

def attractions_index(request):
  attractions = Attraction.objects.all()
  query = request.GET.get('q')
  api_key = os.environ['GOOGLE_PLACES_API_KEY']
  base_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
  params = {
      "input": query,
      "inputtype": "textquery",
      "fields": "name,formatted_address,photos",
      "key": api_key,
  }
  response = requests.get(base_url, params=params)
  save_photo = ''
  for photo in response.json()['candidates']:
    for photos in photo['photos']:
      save_photo = photos['photo_reference']
  photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={save_photo}&key={os.environ['GOOGLE_PLACES_API_KEY']}"
  response1 = requests.get(photo_url)
  if response.status_code == 200:
    return render(request, 'attractions/attractionindex.html', {
      'response': response.json(),  # Return JSON response with place information
      'photo_url': photo_url,
      'attractions': attractions
    })
  else:
    return render(request, 'attractions/attractionindex.html', {
       'attractions': attractions,
      'response': JsonResponse({"error": "Failed to fetch place information."}, status=500)
    })

@login_required
def attractions_detail(request, attraction_id):
  attraction = Attraction.objects.get(id=attraction_id)
  review_form = ReviewForm()
  return render(request, 'attractions/attractiondetail.html', {
    'attraction': attraction,
    'review_form': review_form
  })

class AttractionCreate(LoginRequiredMixin, CreateView):
  model = Attraction
  fields = ['name', 'location']

def save_attraction(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    location = request.POST.get('location')
    photo = request.POST.get('photo')
    new_attraction = Attraction.objects.create(
        name = name,
        location = location,
        photo = photo
    )

    return redirect('/attractions')
  else:
    return redirect('/attractions')


class AttractionUpdate(LoginRequiredMixin, UpdateView):
   model = Attraction
   fields = ['name', 'location']


class AttractionDelete(LoginRequiredMixin, DeleteView):
   model = Attraction
   success_url = '/attractions'

@login_required
def add_review(request, attraction_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.attraction_id = attraction_id
    new_review.user_id = request.user.id
    new_review.save()
  return redirect('attractiondetail', attraction_id=attraction_id)

@login_required
def add_list(request, itinerary_id):
  form = ListForm(request.POST)
  if form.is_valid():
    new_list = form.save(commit=False)
    new_list.itinerary_id = itinerary_id
    new_list.save()
  return redirect('detail', itinerary_id=itinerary_id)

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fetch_and_save_attractions(keyword='restaurants', location='New York')
        self.stdout.write(self.style.SUCCESS('Attractions fetched and saved successfully!'))

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

