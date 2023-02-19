from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
from .models import UserDonation
import stripe


# Create your views here.
def donations(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    donation = UserDonation.objects.all()
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {"price": "price_1McvzzLSo0dYutjcSSSQo0TS", "quantity": 1},
        ],
        mode="subscription",
        success_url="https://8000-kat24c-sanctuary-t3ec7b7nwuf.ws-eu87.gitpod.io/donations/success",
        cancel_url="https://8000-kat24c-sanctuary-t3ec7b7nwuf.ws-eu87.gitpod.io/sanctuary_home/index",
    )

    context = {
        'donation': donation,
        'session_id': session.id,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    }
    return render(request, 'donations/donation.html',   context)


def success(request, args):
    amount = args
    return render(request, 'donations/success.html', {'amount': amount})