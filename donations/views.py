from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse

import stripe


# Create your views here.
def donations(request):
    return render(request, 'donations/donation.html')


def donation_payment(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        amount = int(request.POST['amount'])
        charge = stripe.Charge.create(
            amount=amount*100,
            currency="gpb",
            description="donation",
        )

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {"amount": amount,
             "quantity": 1},
        ],
        mode="payment",
        success_url="https://8000-kat24c-sanctuary-t3ec7b7nwuf.ws-eu87.gitpod.io/donations/success/",
        cancel_url="https://8000-kat24c-sanctuary-t3ec7b7nwuf.ws-eu87.gitpod.io/sanctuary_home/index",
    )

    context = {
        'session_id': session.id,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'donations/donation.html', context)


def success(request, args):
    amount = args
    return render(request, 'donations/success.html', {'amount': amount})
