from django.urls import path
from . import views

urlpatterns = [
    path('', views.adoption, name='adoption'),
    path('adoption_sent', views.adoption_sent, name='adoption_sent'),   
]
