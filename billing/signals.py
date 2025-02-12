from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils.timezone import now
from .models import Payment, UserSubscription
from course_management.models import Course
from notifications.models import Notification

# Grant Course Access After Successful Payment
@receiver(post_save, sender=Payment)
def grant_course_access(sender, instance, created, **kwargs):
    if instance.status == "completed" and instance.course:
        student = instance.user
        course = instance.course

        # Enroll the student in the course
        student.student_profile.enrolled_courses.add(course)
        student.save()

        # Send notification
        Notification.objects.create(user=student, message=f"You have been enrolled in {course.title}.")

# Activate Subscription After Payment
@receiver(post_save, sender=UserSubscription)
def activate_subscription(sender, instance, created, **kwargs):
    if created and instance.is_active:
        student = instance.user

        # Send notification
        Notification.objects.create(user=student, message=f"Your subscription for {instance.plan.name} is active.")

# Deactivate Subscription on Expiration
@receiver(pre_delete, sender=UserSubscription)
def deactivate_subscription(sender, instance, **kwargs):
    student = instance.user

    # Remove course access
    student.student_profile.enrolled_courses.clear()
    student.save()

    # Send notification
    Notification.objects.create(user=student, message="Your subscription has expired. Please renew to continue accessing courses.")

# Handle Failed Payment (Revoke Access)
@receiver(post_save, sender=Payment)
def handle_failed_payment(sender, instance, **kwargs):
    if instance.status == "failed":
        student = instance.user
        Notification.objects.create(user=student, message="Your payment failed. Please retry to continue access.")

# Notify Users Before Subscription Expiry
@receiver(post_save, sender=UserSubscription)
def notify_subscription_expiry(sender, instance, **kwargs):
    days_remaining = (instance.end_date - now().date()).days
    if days_remaining <= 5:  # Notify 5 days before expiry
        Notification.objects.create(user=instance.user, message="Your subscription is about to expire. Renew now!")
