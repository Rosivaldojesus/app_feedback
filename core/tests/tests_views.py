from django.urls import reverse
from django.test import TestCase

# Create your tests here.

class HomeViewTestCase(TestCase):

    def test_status_code_200(self):
        response = self.client.get(reverse('core:core_view'))
        self.assertEqual(response.status_code, 200)
