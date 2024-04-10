from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('itinerarys/', views.itinerarys_index, name='index'),
    path('itinerarys/<int:itinerary_id>/', views.itinerarys_detail, name='detail'),
    path('itinerarys/create/', views.ItineraryCreate.as_view(), name='itinerarys_create'),
    path('itinerarys/<int:pk>/update/', views.ItineraryUpdate.as_view(), name='itinerarys_update'),
    path('itinerarys/<int:pk>/delete/', views.ItineraryDelete.as_view(), name='itinerarys_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('itinerarys/<int:itinerary_id>/add_list/', views.add_list, name='add_list'),
    path('attractions/', views.AttractionList.as_view(), name='attractions_index'),
]