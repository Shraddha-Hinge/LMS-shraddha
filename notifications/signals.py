from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
from course_management.models import Course
from billing.models import Payment
from live_sessions.models import LiveSession
from .email_service import send_email_notification
from .sms_service import send_sms_notification

# Notify Students About Course Enrollment
@receiver(post_save, sender=Course)
def notify_course_enrollment(sender, instance, created, **kwargs):
    if created:
        for student in instance.students.all():
            message = f"You have been enrolled in {instance.title}."
            Notification.objects.create(user=student, message=message)
            send_email_notification(student, message)

# Notify Admin on Payment Completion
@receiver(post_save, sender=Payment)
def notify_payment_completion(sender, instance, **kwargs):
    if instance.status == "completed":
        message = f"Payment of ${instance.amount} completed successfully."
        Notification.objects.create(user=instance.user, message=message)
        send_email_notification(instance.user, message)

# Notify Students About Upcoming Live Session
@receiver(post_save, sender=LiveSession)
def notify_live_session(sender, instance, created, **kwargs):
    if created:
        for student in instance.batch.studentprofile_set.all():
            message = f"Upcoming live session: {instance.title} on {instance.scheduled_time}."
            Notification.objects.create(user=student.student, message=message)
            send_email_notification(student.student, message)
