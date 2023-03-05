from django.shortcuts import get_object_or_404
from django.conf import settings
from products.models import Product


def bag_contents(request):
    bag_items = []
    total = 0
    bag = request.session.get('bag', {})

    for don_id, don_data in bag.items():
        if isinstance(don_data, int):
            product = get_object_or_404(Product, pk=don_id)
            total = product.price
            bag_items.append({
                'product': product,
            })

    context = {
        'bag_items': bag_items,
        'total': total,
    }

    return context
