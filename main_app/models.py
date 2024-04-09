from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


# Create your models here.
class Itinerary(models.Model):
  name = models.CharField(max_length=100)
  date_from = models.DateField('Travel From')
  date_to = models.DateField('Travel To')
  location = models.CharField()
  description = models.TextField(max_length=250)

  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'itinerary_id': self.id})

  def list_assigned(self):
    return self.list_set.filter(date=date.today()).count() >= 1

class List(models.Model):
  date = models.DateField()
  time = models.TimeField()
  location = models.CharField()

  itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.location} on {self.date}'

  class Meta:
    ordering = ['-date']

   