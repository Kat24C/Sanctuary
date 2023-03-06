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
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    bag[don_id] = quantity

    request.session['bag'] = bag
    return redirect('checkout')


def remove_from_bag(request, don_id):
    """Remove the item from the bag"""
    try:
        product = get_object_or_404(Product, pk=don_id)
        bag = request.session.get('bag', {})
        del bag[don_id]
        bag.pop(don_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def error_404_view(request, exception):
    return render(request, '404.html')
