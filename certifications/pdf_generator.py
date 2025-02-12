from io import BytesIO
from django.core.files.base import ContentFile
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Certificate

def generate_certificate(student, course):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setFont("Helvetica-Bold", 20)
    p.drawString(150, 750, "Certificate of Completion")
    p.setFont("Helvetica", 14)
    p.drawString(150, 700, f"This is to certify that {student.get_full_name()}")
    p.drawString(150, 670, f"has successfully completed the course: {course.title}")
    p.drawString(150, 640, f"Issue Date: {course.certificates.filter(student=student).first().issue_date}")

    p.save()
    buffer.seek(0)
    certificate = Certificate.objects.create(student=student, course=course)
    certificate.certificate_file.save(f"certificate_{certificate.certificate_id}.pdf", ContentFile(buffer.getvalue()))
    buffer.close()
    return certificate
