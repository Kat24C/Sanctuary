from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal_home_pg, name='animals_home'),
    path('edit_mission/', views.edit_mission, name='edit_mission')
]
