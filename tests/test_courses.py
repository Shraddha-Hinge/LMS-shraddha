from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import User
from course_management.models import Course, Batch

class CourseTests(APITestCase):
    def setUp(self):
        self.student = User.objects.create_user(email="student@example.com", password="TestPass123", role="student")
        self.staff = User.objects.create_user(email="staff@example.com", password="TestPass123", role="staff")
        self.instructor = User.objects.create_user(email="instructor@example.com", password="TestPass123", role="staff")
        self.course = Course.objects.create(title="Django Course", description="Learn Django")
        self.batch = Batch.objects.create(name="Batch A", course=self.course, instructor=self.staff)
        self.client.force_authenticate(user=self.student)

    def test_student_enrollment(self):
        response = self.client.post(f"/api/course_management/enroll/{self.course.id}/")
        self.course = Course.objects.create(title="Django Course", description="Learn Django", instructor=self.instructor)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.student.studentprofile.enrolled_courses.filter(id=self.course.id).exists())

    def test_course_completion_tracking(self):
        self.student.studentprofile.progress[self.course.id] = 100
        self.student.studentprofile.save()
        self.assertEqual(self.student.studentprofile.progress[self.course.id], 100)
