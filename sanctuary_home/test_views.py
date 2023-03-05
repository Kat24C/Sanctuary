from django.test import TestCase
from .models import HomePage
from . import views
# Create your tests here.


class TestViews(TestCase):
   
    def test_animal_about_page(self):
        """
        Test to ensure all the information is shown
        """

        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sanctuary_home/about.html')

    def test_edit_mission(self):
        response = self.client.get(f'/edit_mission/{self.info.id}')
        self.client.post(f'/edit_mission/{self.info.id}', {
            'heading': 'Edited',
            'statement': 'Test Statement',
        })
        edit = HomePage.objects.first().heading
        self.assertEqual(edit, "Edited")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sanctuary_home/staff_form.html')
