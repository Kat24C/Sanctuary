from django.test import TestCase
from .models import AboutTheAnimal


# Create your tests here.
class TestViewsAnimals(TestCase):
    def test_adoption_gets_pets(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'animals/pet_info.html')
