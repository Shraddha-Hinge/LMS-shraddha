from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Attendance

@receiver(pre_save, sender=Attendance)
def prevent_duplicate_attendance(sender, instance, **kwargs):
    existing_attendance = Attendance.objects.filter(session=instance.session, student=instance.student).exists()
    if existing_attendance:
        raise ValueError("Attendance already marked for this session")
