from django.db.models.signals import post_save
from django.dispatch import receiver
from course_management.models import Course
from .models import Certificate
from .pdf_generator import generate_certificate

@receiver(post_save, sender=Course)
def issue_certificate_on_completion(sender, instance, **kwargs):
    if instance.is_archived:  # Assume archived courses are completed
        for student in instance.batches.all().values_list("students", flat=True):
            student = User.objects.get(id=student)
            if not Certificate.objects.filter(student=student, course=instance).exists():
                generate_certificate(student, instance)
