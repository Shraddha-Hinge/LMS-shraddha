from django.core.mail import send_mail
from django.conf import settings

def send_email_notification(user, message):
    if user.notification_preferences.receive_email:
        send_mail(
            subject="LMS Notification",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )
