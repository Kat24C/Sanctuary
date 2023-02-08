from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal_home_pg, name='animals_home_pg'),
    path('edit_mission/<int:info_id>', views.edit_mission, name='edit_mission')
]
