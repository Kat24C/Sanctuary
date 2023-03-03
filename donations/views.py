from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


import stripe
import json

stripe_public_key = settings.STRIPE_PUBLIC_KEY
stripe.api_key = settings.STRIPE_SECRET_KEY


def donations(request):
    return render(request, 'donations/donations.html')


def cancel(request):
    pass


def donation_pay(request):
    if request.method == 'POST':
        print('Data:', request.POST)
        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            name=request.POST['name'],
            email=request.POST['email'],
            source=request.POST['stripeToken'],
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='eur',
            description='Donation',
        )
    return redirect('success')


def success(request):
    messages.success(request, 'Thank you for your donation.')
    return render(request, 'donations/success.html')
