from django.urls import path
from . import views

urlpatterns = [
    path('', views.donation_detail, name='donation_detail'),
]
