from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .models import Product

import json
import stripe
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY


def donation_detail(request):
    """ A view to show individual product details """

    product = Product.objects.all()
    messages.success(request, 'Please help us by donating')
    context = {
        'product': product,
        "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
    }

    return render(request, 'products/donation_detail.html', context)
