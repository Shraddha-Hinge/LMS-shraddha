import uuid
from django.db import models
from accounts.models import User
from course_management.models import Course

# Certificate Model
class Certificate(models.Model):
    certificate_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="certificates")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="certificates")
    issue_date = models.DateField(auto_now_add=True)
    certificate_file = models.FileField(upload_to="certificates/")

    def __str__(self):
        return f"Certificate {self.certificate_id} - {self.student.email} - {self.course.title}"
