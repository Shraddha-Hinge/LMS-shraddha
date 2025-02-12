import csv
from io import StringIO
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import StudentPerformance

# Export Student Performance Report as CSV
def export_student_performance_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="student_performance.csv"'

    writer = csv.writer(response)
    writer.writerow(["Student", "Course", "Completion %", "Average Score", "Attendance %"])

    for record in StudentPerformance.objects.all():
        writer.writerow([record.student.email, record.course.title, record.completion_percentage, record.avg_test_score, record.attendance_rate])

    return response

# Export Student Performance Report as PDF
def export_student_performance_pdf(request):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="student_performance.pdf"'

    pdf = canvas.Canvas(response)
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(200, 750, "Student Performance Report")
    pdf.setFont("Helvetica", 12)

    y = 720
    for record in StudentPerformance.objects.all():
        pdf.drawString(50, y, f"{record.student.email} - {record.course.title} - {record.completion_percentage}% Completed")
        y -= 20

    pdf.save()
    return response
