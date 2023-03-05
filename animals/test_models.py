from django.test import TestCase
from django.urls import path, reverse
from .models import AboutTheAnimal
from . import views


# Create your tests here.
class TestModelAdoption(TestCase):

    def test_animal_string_method_returns_name(self):
        animal = AboutTheAnimal.objects.create(animals_name='Liq')
        self.assertEqual(str(animal), 'Liq')

    def test_animals_return_reverse(self):
        animal = AboutTheAnimal.objects.get(id=1)
        self.assertEqual(animal.get_absolute_url(), 'animals/pet_info/1')
