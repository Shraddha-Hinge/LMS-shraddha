from django.db import models
from accounts.models import User
from course_management.models import Batch

# Chat Message Model
class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages_sent")
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name="batch_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.email} - {self.batch.name}: {self.content[:20]}"

# Announcement Model
class Announcement(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="announcements")
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.email} - {self.title}"

# Notification Model
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comm_notifications")   
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.message[:20]}"
