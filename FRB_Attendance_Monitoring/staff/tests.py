from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponse

# Create your tests here.

class ViewsTest(TestCase):
    def test_index_view(self):
        # Test the 'index' view
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_staff_dashboard_view(self):
        # Test the 'staff_dashboard' view
        response = self.client.get(reverse('staff_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff_dashboard.html')

    def test_admincontact_view(self):
        # Test the 'admincontact' view
        response = self.client.get(reverse('admincontact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
