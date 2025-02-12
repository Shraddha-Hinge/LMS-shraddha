from django.db import models
from accounts.models import User

# Notification Model
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notif_notifications")  
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.message[:20]}"

# User Notification Preferences Model
class NotificationPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="notification_preferences")
    receive_email = models.BooleanField(default=True)
    receive_sms = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.email} - Email: {self.receive_email}, SMS: {self.receive_sms}"
