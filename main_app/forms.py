from django.forms import ModelForm
from .models import List, Review

class ListForm(ModelForm):
  class Meta:
    model = List
    fields = ['date', 'time', 'attraction']

class ReviewForm(ModelForm):
  class Meta:
    model = Review
    fields = ['user', 'review', 'rating']
