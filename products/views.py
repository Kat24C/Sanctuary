from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Product

# Create your views here.


def donation_detail(request):
    """ A view to show individual product details """

    product = Product.objects.all()

    context = {
        'product': product,
    }

    return render(request, 'products/donation_detail.html', context)
