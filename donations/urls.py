from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('<don_id>', views.donations, name='donations'),
    path('success', views.success, name='success'),
#    path('wh/', webhook, name='webhook'),

]
