from django.db import models
from accounts.models import User

# Course Model
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# Batch Model
class Batch(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="batches")
    tutor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="batches")
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.course.title}"

# Syllabus Progress Model
class SyllabusProgress(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name="syllabus_progress")
    topic = models.CharField(max_length=255)
    is_unlocked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.topic} - {self.batch.name}"
