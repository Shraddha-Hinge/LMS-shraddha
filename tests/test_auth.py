from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import User

class AuthTests(APITestCase):
    def setUp(self):
        self.register_url = "/api/accounts/register/"
        self.login_url = "/api/accounts/login/"
        self.user_data = {"email": "testuser@example.com", "password": "TestPass123"}
        self.client.post(self.register_url, self.user_data)

    def test_register_user(self):
        response = self.client.post(self.register_url, {"email": "newuser@example.com", "password": "NewPass123"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        response = self.client.post(self.login_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)  # Ensure JWT token is returned
