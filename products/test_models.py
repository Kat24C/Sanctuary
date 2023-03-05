from django.test import TestCase
from .models import Product
from . import views


# Create your tests here.
class TestModelProduct(TestCase):
    def test_product_string_method_returns_name(self):
        product = Product.objects.create(name='Test')
        self.assertEqual(str(product), 'Test')

    def test_product_display_price(self):
        get_display_price = sum(1000/100 == 10.00)
