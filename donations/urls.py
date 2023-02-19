from django.urls import path
from . import views

urlpatterns = [
    path('', views.donations, name='donations'),
    path('donation_payment', views.donation_payment, name='donation_payment'),
    path('success/<str:args>', views.success, name='success'),
]
