from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.http import Http404

class AccountsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com'
        )

    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    # Add more tests for other views as needed...

    def test_custom_404_handling(self):
        with self.assertRaises(Http404):
            response = self.client.get('/nonexistent-url/')

    def test_custom_500_handling(self):
        response = self.client.get(reverse('nonexistent-view'))
        self.assertEqual(response.status_code, 500)