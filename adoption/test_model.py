from django.test import TestCase
from django.urls import path, reverse
from .models import AdoptionQuestion
from . import views


# Create your tests here.
class TestModelAdoption(TestCase):

    def test_adoption_string_method_returns_perspective_name(self):
        adoption = AdoptionQuestion.objects.create(perspective_pet_parent='Mary')
        self.assertEqual(str(adoption), 'Mary')
