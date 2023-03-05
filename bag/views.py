from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product
from django.http import JsonResponse, HttpResponse

import stripe


# Create your views here.
def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, don_id):

    product = get_object_or_404(Product, pk=don_id)
    quantity = 1
    total = product.price
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    bag[don_id] = quantity

    request.session['bag'] = bag
    return redirect('donations')

