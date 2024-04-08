from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('itineraries/', views.itineraries_index, name='index'),
    path('itineraries/<int:itinerary_id>/', views.itineraries_detail, name='detail'),
]