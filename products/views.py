from django.shortcuts import render
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
