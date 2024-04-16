from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('itinerarys/', views.itinerarys_index, name='index'),
    path('itinerarys/<int:itinerary_id>/', views.itinerarys_detail, name='detail'),
    path('itinerarys/create/', views.ItineraryCreate.as_view(), name='itinerarys_create'),
    path('itinerarys/<int:pk>/update/', views.ItineraryUpdate.as_view(), name='itinerarys_update'),
    path('itinerarys/<int:pk>/delete/', views.ItineraryDelete.as_view(), name='itinerarys_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('itinerarys/<int:itinerary_id>/assoc_attraction/<int:attraction_id>/', views.assoc_attraction, name='assoc_attraction'),
    path('itinerarys/<int:itinerary_id>/unassoc_attraction/<int:attraction_id>/', views.unassoc_attraction, name='unassoc_attraction'),
    path('attractions/', views.attractions_index, name='attractionindex'),
    path('attractions/<int:attraction_id>/', views.attractions_detail, name='attractiondetail'),
    path('attractions/create/', views.AttractionCreate.as_view(), name='attractions_create'),
    path('attractions/<int:pk>/update/', views.AttractionUpdate.as_view(), name='attractions_update'),
    path('attractions/<int:pk>/delete/', views.AttractionDelete.as_view(), name='attractions_delete'),
    path('attractions/<int:attraction_id>/add_review/', views.add_review, name='add_review'),
    path('attractions/save_attraction', views.save_attraction, name='save_attraction'),
    path('myitinerarys/', views.itinerarys_userindex, name='itinerarys_userindex'),
]