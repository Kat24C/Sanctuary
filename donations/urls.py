from django.urls import path
from . import views

urlpatterns = [
    path('', views.donations, name='donations'),
    path('donations_pay', views.donations_pay, name='donations_pay'),
    path('donations_successful', views.donations_successful, name='donations_successful'),
]
