from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('animals/', views.animal_outline, name='animal_outline'),
    path('wild_animals/', views.wild_animals, name='wild_animals'),
    path('farm_animals/', views.farm_animals, name='farm_animals'),
    path('pets/', views.pets, name='pets'),
]
