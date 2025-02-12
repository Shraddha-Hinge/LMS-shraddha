from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Certificate
from .serializers import CertificateSerializer
from accounts.permissions import IsStudent, IsAdmin
from .pdf_generator import generate_certificate

# List Certificates for a Student
class CertificateListView(generics.ListAPIView):
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated, IsStudent]

    def get_queryset(self):
        return Certificate.objects.filter(student=self.request.user)

# Admin: Generate Certificate Manually
class AdminGenerateCertificateView(generics.CreateAPIView):
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def create(self, request, *args, **kwargs):
        student_id = request.data.get("student_id")
        course_id = request.data.get("course_id")

        try:
            student = User.objects.get(id=student_id)
            course = Course.objects.get(id=course_id)

            if Certificate.objects.filter(student=student, course=course).exists():
                return Response({"error": "Certificate already exists"}, status=status.HTTP_400_BAD_REQUEST)

            certificate = generate_certificate(student, course)
            return Response({"message": "Certificate generated successfully", "certificate_id": str(certificate.certificate_id)}, status=status.HTTP_201_CREATED)

        except User.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

# Download Certificate (PDF)
class CertificateDownloadView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsStudent]

    def get(self, request, *args, **kwargs):
        certificate_id = kwargs.get("certificate_id")
        try:
            certificate = Certificate.objects.get(certificate_id=certificate_id, student=request.user)
            response = Response()
            response["Content-Disposition"] = f'attachment; filename="{certificate.certificate_file.name}"'
            response["Content-Type"] = "application/pdf"
            response.content = certificate.certificate_file.read()
            return response
        except Certificate.DoesNotExist:
            return Response({"error": "Certificate not found"}, status=status.HTTP_404_NOT_FOUND)
