from decimal import Decimal
from django.conf import settings



def bag_contents(request):

    bag_items = []
    total = bag_items

    context = {
        'bag_items': bag_items,
        'total': total,
    }

    return context
