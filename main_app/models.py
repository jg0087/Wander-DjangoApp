from django.db import models
from django.urls import reverse
from datetime import date, datetime
from django.utils import timezone
from django.contrib.auth.models import User

RATINGS = (
  ('1', '1'),
  ('2', '2'),
  ('3', '3'),
  ('4','4'),
  ('5', '5')
)



# Create your models here.
class Attraction(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=100)
  photo = models.TextField(max_length=1000)
  
  
  def __str__(self):
    return f'{self.name}'
  
  def get_absolute_url(self):
    return reverse('attractions/attractiondetail', kwargs={'attraction_id': self.id})
  

    
class Itinerary(models.Model):
  name = models.CharField(max_length=100)
  date_from = models.DateField('Travel From')
  date_to = models.DateField('Travel To')
  location = models.CharField()
  description = models.TextField(max_length=250)

  attractions = models.ManyToManyField(Attraction)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name}'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'itinerary_id': self.id})

  def list_assigned(self):
    return self.list_set.filter(date=date.today()).count() >= 1
  

class Review(models.Model):
  review = models.CharField(max_length=100)
  rating = models.CharField(max_length=1, choices=RATINGS, default=RATINGS[0][0])

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.user} left a rating of {self.get_rating_display()} on {self.attraction}"

  def get_absolute_url(self):
    return reverse('attractions_detail', kwargs={'pk': self.id})