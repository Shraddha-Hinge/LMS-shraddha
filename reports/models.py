from django.db import models
from accounts.models import User
from course_management.models import Course

# Student Performance Model
class StudentPerformance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="performance")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="performance")
    completion_percentage = models.FloatField(default=0.0)
    avg_test_score = models.FloatField(default=0.0)
    attendance_rate = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.student.email} - {self.course.title} ({self.completion_percentage}%)"

# Platform Analytics Model
class PlatformAnalytics(models.Model):
    total_students = models.IntegerField(default=0)
    active_courses = models.IntegerField(default=0)
    total_revenue = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Platform Analytics (Updated: {self.updated_at})"
