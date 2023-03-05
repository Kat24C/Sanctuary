from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse, HttpResponse

from .forms import DonateForm
from .models import Donation, DonTot
from products.models import Product
from bag.contexts import bag_contents

import stripe
import json

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)
        

def donations(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        don_form = DonateForm()
        if don_form.is_valid():
            donate = don_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            donate.stripe_pid = pid
            donate.original_bag = json.dumps(bag)
            donate.save()
            return redirect(reverse('success'))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})

        current_bag = bag_contents(request)
        total = current_bag['total']
        stripe_total = 1000
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency='eur',
        )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    context = {
        'intent': intent,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, 'checkout/donations.html', context)


def success(request):
    """
    Handle successful checkouts
    """
    messages.success(request, 'Thank you')

    return render(request, 'checkout/success.html')
