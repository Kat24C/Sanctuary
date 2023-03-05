from django.test import TestCase
from django.urls import path, reverse
from .models import AdoptionQuestion
from . import views


# Create your tests here.
class TestViewsAdoption(TestCase):

    def test_get_adoption_form(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adoption/adoption_form.html')

    def test_adoption_send_mail(self):
        pass

    def test_adoption_return_form(self):
        pass

    def test_adoption_return_success(self):
        response = self.client.get('adoption_sent')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adoption/success.html')