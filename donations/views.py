from django.shortcuts import render
from django.conf import settings

import stripe

stripe_public_key = settings.STRIPE_PUBLIC_KEY
stripe_secret_key = settings.STRIPE_SECRET_KEY


def donations(request):
    return render(request, 'donations/donations.html')


def donations_pay(request):
    pass


def donations_successful(request):
    pass
