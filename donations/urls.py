from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.donations, name='donations'),
    path('donation_pay', views.donation_pay, name='donation_pay'),
    path('success', views.success, name='success'),
    path('wh/', webhook, name='webhook'),
]
