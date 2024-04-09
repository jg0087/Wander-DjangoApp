from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Itinerary
from django.contrib.auth import login

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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

@login_required
def itinerarys_user_index(request):
  itinerarys = Itinerary.objects.filter(user=request.user)
  return render(request, 'itinerarys/user/index.html', {
    'itinerarys': itinerarys
  })

def itinerarys_detail(request, itinerary_id):
   itinerary = Itinerary.objects.get(id=itinerary_id)
   return render(request, 'itinerarys/detail.html', {
      'itinerary': itinerary
   })


class ItineraryCreate(LoginRequiredMixin, CreateView):
   model = Itinerary
   fields = ['name', 'date_from', 'date_to', 'location', 'description']
   def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)



class ItineraryUpdate(LoginRequiredMixin, UpdateView):
   model = Itinerary
   fields = '__all__'


class ItineraryDelete(LoginRequiredMixin, DeleteView):
   model = Itinerary
   success_url = '/itinerarys'


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

