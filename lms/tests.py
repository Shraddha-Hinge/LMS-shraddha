from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@example.com", password="password", role="student")

    def test_user_creation(self):
        self.assertEqual(self.user.email, "test@example.com")

    def test_user_role(self):
        self.assertEqual(self.user.role, "student")
