from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Product

import json
import stripe
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY


def donation_detail(request):
    """ A view to show individual product details """

    product = Product.objects.all()

    context = {
        'product': product,
        "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
    }

    return render(request, 'products/donation_detail.html', context)
