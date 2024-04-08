from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('itineraries/', views.itineraries_index, name='index'),
    path('itineraries/create/', views.ItineraryCreate.as_view(), name='itineraries_create'),
    path('itineraries/<int:pk>/update/', views.ItineraryUpdate.as_view(), name='itineraries_update'),
    path('itineraries/<int:pk>/delete/', views.ItineraryDelete.as_view(), name='itineraries_delete'),
]