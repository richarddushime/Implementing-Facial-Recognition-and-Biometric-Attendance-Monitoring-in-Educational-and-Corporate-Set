from django.test import TestCase
from django.urls import reverse
# Create your tests here.
class IndexViewTest(TestCase):
    def test_index_view(self):
        # Use the reverse function to get the URL for the 'index' view
        url = reverse('home')

        # Perform a GET request to the 'index' view
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the 'home.html' template is used in the response
        self.assertTemplateUsed(response, 'home.html')
