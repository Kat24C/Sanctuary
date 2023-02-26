from django.urls import path
from . import views

urlpatterns = [
    path('', views.donations, name='donations'),
    path('donation_pay', views.donation_pay, name='donation_pay'),
    path('donations_successful', views.donations_successful, name='donations_successful'),
    path('stripe_webhook', views.stripe_webhook, name='stripe_webhook'),
]
