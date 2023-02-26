from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def donations(request):
    return render(request, 'donations/donations.html')


def donation_cancelled(request):
    pass


def donation_pay(request):
    if request.method == "POST":
        amount = request.POST['amount']
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': amount,
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('donations_successful')) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri(reverse('donation_cancelled')),
        )

        return JsonResponse({
            'session_id': session.id,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY
        })
        

def donations_successful(request):
    return render(request, 'donations/donations_successful.html')


@csrf_exempt
def stripe_webhook(request):

    print('WEBHOOK!')
    # You can find your endpoint's secret in your webhook settings
    endpoint_secret = 'whsec_Xj8wBk2qiUcjDEmYu5kfKkOrJCJ5UUjW'

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(session)
        line_items = stripe.checkout.Session.list_line_items(session['id'], limit=1)
        print(line_items)

    return HttpResponse(status=200)
