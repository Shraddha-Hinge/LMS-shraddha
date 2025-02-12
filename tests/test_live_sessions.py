from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import User
from course_management.models import Course, Batch
from live_sessions.models import LiveSession, Attendance

class LiveSessionTests(APITestCase):
    def setUp(self):
        self.staff = User.objects.create_user(email="staff@example.com", password="TestPass123", role="staff")
        self.student = User.objects.create_user(email="student@example.com", password="TestPass123", role="student")
        self.course = Course.objects.create(title="Django Course")
        self.batch = Batch.objects.create(name="Batch A", course=self.course, instructor=self.staff)
        self.session = LiveSession.objects.create(title="Live Django Class", batch=self.batch, tutor=self.staff, meeting_link="https://zoom.com/123", scheduled_time="2025-03-01T10:00:00Z")

    def test_schedule_live_session(self):
        self.client.force_authenticate(user=self.staff)
        response = self.client.post("/api/live_sessions/schedule/", {"title": "New Live Class", "batch": self.batch.id, "tutor": self.staff.id, "meeting_link": "https://meet.google.com/xyz", "scheduled_time": "2025-03-10T10:00:00Z"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_mark_attendance(self):
        self.client.force_authenticate(user=self.student)
        response = self.client.post("/api/live_sessions/attendance/", {"session": self.session.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Attendance.objects.filter(student=self.student, session=self.session).exists())
