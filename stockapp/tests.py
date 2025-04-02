from django.test import TestCase
from django.urls import reverse

class URLTests(TestCase):
    def test_login_url(self):
        """Test if the login page loads successfully."""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_signup_url(self):
        """Test if the signup page loads successfully."""
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
