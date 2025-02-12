from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import User

class RoleTests(APITestCase):
    def setUp(self):
        self.student = User.objects.create_user(email="student@example.com", password="TestPass123", role="student")
        self.staff = User.objects.create_user(email="staff@example.com", password="TestPass123", role="staff")
        self.admin = User.objects.create_user(email="admin@example.com", password="TestPass123", role="admin")

    def test_student_cannot_access_staff_api(self):
        self.client.force_authenticate(user=self.student)
        response = self.client.get("/api/course_management/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_access_all_apis(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get("/api/course_management/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
