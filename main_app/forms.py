from django.forms import ModelForm
from .models import Attraction, Review

class AttractionForm(ModelForm):
  class Meta:
    model = Attraction
    fields = ['name']

class ReviewForm(ModelForm):
  class Meta:
    model = Review
    fields = ['review', 'rating']
