from django.db import models
from django.urls import reverse


# Create your models here.
class Itinerary(models.Model):
  name = models.CharField(max_length=100)
  date_from = models.DateField('Travel From')
  date_to = models.DateField('Travel To')
  location = models.CharField()
  description = models.TextField(max_length=250)

  # no makemigrations is necessary
  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'itinerary_id': self.id})
