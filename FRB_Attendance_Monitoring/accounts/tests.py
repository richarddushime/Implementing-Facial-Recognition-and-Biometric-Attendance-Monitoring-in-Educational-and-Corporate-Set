from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import CustomUser  # Import your models
from .views import account_login, account_register, account_logout
# Create your tests here.

class YourAppTestCase(TestCase):
    def setUp(self):
        # Set up any data needed for the tests
        self.user_data = {
            'email': 'testuser@example.com',
            'password': 'testpassword',
        }
        self.staff_user = CustomUser.objects.create_user(email='staff@example.com', password='staffpass', user_type=1)
        self.student_user = CustomUser.objects.create_user(email='student@example.com', password='studentpass', user_type=2)

    def test_account_login_authenticated_staff_redirect(self):
        # Test that an authenticated staff user is redirected to the staff dashboard
        self.client.force_login(self.staff_user)
        response = self.client.get(reverse('account_login'))
        self.assertRedirects(response, reverse('staffDashboard'))

    def test_account_login_authenticated_student_redirect(self):
        # Test that an authenticated student user is redirected to the student dashboard
        self.client.force_login(self.student_user)
        response = self.client.get(reverse('account_login'))
        self.assertRedirects(response, reverse('studentDashboard'))

    def test_account_login_valid_credentials_redirect_staff(self):
        # Test login with valid staff credentials
        response = self.client.post(reverse('account_login'), self.user_data)
        self.assertRedirects(response, reverse('staffDashboard'))

    def test_account_login_valid_credentials_redirect_student(self):
        # Test login with valid student credentials
        self.user_data['email'] = 'student@example.com'
        self.user_data['password'] = 'studentpass'
        response = self.client.post(reverse('account_login'), self.user_data)
        self.assertRedirects(response, reverse('studentDashboard'))

    def test_account_login_invalid_credentials(self):
        # Test login with invalid credentials
        self.user_data['password'] = 'invalidpass'
        response = self.client.post(reverse('account_login'), self.user_data)
        self.assertContains(response, "Invalid details")

    def test_account_register_valid_data_redirect(self):
        # Test registration with valid data
        user_data = {
            'email': 'newuser@example.com',
            'password': 'newuserpass',
        }
        response = self.client.post(reverse('account_register'), user_data)
        self.assertRedirects(response, reverse('account_login'))

    def test_account_register_invalid_data(self):
        # Test registration with invalid data
        user_data = {
            'email': 'invalid_email',
            'password': 'short',
        }
        response = self.client.post(reverse('account_register'), user_data)
        self.assertContains(response, "Provided data failed validation")

    def test_account_logout_authenticated_user(self):
        # Test logout when a user is authenticated
        self.client.force_login(self.staff_user)
        response = self.client.get(reverse('account_logout'))
        self.assertRedirects(response, reverse('account_login'))

    def test_account_logout_unauthenticated_user(self):
        # Test logout when no user is authenticated
        response = self.client.get(reverse('account_logout'))
        self.assertRedirects(response, reverse('account_login'))
        # You can also check for the success message in the response.
