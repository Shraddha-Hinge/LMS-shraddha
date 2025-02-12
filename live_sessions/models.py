from django.db import models
from accounts.models import User
from course_management.models import Batch

# Live Session Model
class LiveSession(models.Model):
    title = models.CharField(max_length=255)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name="live_sessions")
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hosted_sessions")
    meeting_link = models.URLField()
    scheduled_time = models.DateTimeField()

    def __str__(self):
        return f"{self.title} - {self.batch.name}"

# Attendance Model
class Attendance(models.Model):
    session = models.ForeignKey(LiveSession, on_delete=models.CASCADE, related_name="attendances")
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="session_attendances")
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.email} - {self.session.title}"
