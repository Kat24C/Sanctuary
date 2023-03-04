from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.donations, name='donations'),
    path('success', views.success, name='success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),

]
