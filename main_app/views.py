from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Itinerary, Attraction
from .forms import ListForm, ReviewForm

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
   return render(request, 'itinerarys/detail.html', {
      'itinerary': itinerary,
      'list_form': list_form
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

@login_required
def add_list(request, itinerary_id):
  form = ListForm(request.POST)
  if form.is_valid():
    new_list = form.save(commit=False)
    new_list.itinerary_id = itinerary_id
    new_list.save()
  return redirect('detail', itinerary_id=itinerary_id)
  

class AttractionList(ListView):
  model = Attraction

class AttractionDetail(LoginRequiredMixin, DetailView):
  model = Attraction
  def attraction_form(request):
    review_form = ReviewForm()

class AttractionCreate(LoginRequiredMixin, CreateView):
  model = Attraction
  fields = ['name', 'location']
   

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
    new_review.save()
  return redirect('attractions_index')

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

