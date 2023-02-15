from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal_outline, name='animal_outline'),
    path('pet_info/<int:pet_id>', views.pet_info, name='pet_info'),
    path('add_pet/', views.add_pet, name='add_pet'),
    path('edit_pet/<int:pet_id>', views.edit_pet, name='edit_pet'),
    path('delete_pet/<int:pet_id>', views.delete_pet, name='delete_pet'),
]
