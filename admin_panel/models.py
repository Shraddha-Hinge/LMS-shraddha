from django.db import models
from accounts.models import User

# Staff Role Model
class StaffRole(models.Model):
    ROLE_CHOICES = (
        ("course_manager", "Course Manager"),
        ("content_manager", "Content Manager"),
        ("announcement_manager", "Announcement Manager"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="staff_role")
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.email} - {self.get_role_display()}"

# Admin Actions Model
class AdminAction(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="admin_actions")
    action = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.admin.email} - {self.action}"
