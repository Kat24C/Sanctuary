from django.test import TestCase
from django.urls import path, reverse
from .models import HomePage
from . import views


# Create your tests here.
class TestModelHomePage(TestCase):

    def test_home_returns_heading(self):
        home = HomePage.objects.create(heading='Test')
        self.assertEqual(str(home), 'Test')
