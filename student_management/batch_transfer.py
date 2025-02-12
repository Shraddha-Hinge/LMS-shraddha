from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import StudentProfile
from course_management.models import Batch
from accounts.permissions import IsStudent, IsAdmin

# Student Request for Batch Transfer
class RequestBatchTransferView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsStudent]

    def update(self, request, *args, **kwargs):
        student_profile = StudentProfile.objects.get(student=request.user)
        new_batch_id = request.data.get("new_batch_id")

        try:
            new_batch = Batch.objects.get(id=new_batch_id)

            # Send request to admin for approval
            student_profile.current_batch = None  # Temporary state until admin approves
            student_profile.save()

            return Response({"message": "Batch transfer request submitted"}, status=status.HTTP_200_OK)
        except Batch.DoesNotExist:
            return Response({"error": "Batch not found"}, status=status.HTTP_404_NOT_FOUND)

# Admin Approves Batch Transfer
class ApproveBatchTransferView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def update(self, request, *args, **kwargs):
        student_id = request.data.get("student_id")
        batch_id = request.data.get("batch_id")

        try:
            student_profile = StudentProfile.objects.get(student_id=student_id)
            new_batch = Batch.objects.get(id=batch_id)

            student_profile.current_batch = new_batch
            student_profile.save()

            return Response({"message": "Batch transfer approved"}, status=status.HTTP_200_OK)
        except StudentProfile.DoesNotExist:
            return Response({"error": "Student profile not found"}, status=status.HTTP_404_NOT_FOUND)
        except Batch.DoesNotExist:
            return Response({"error": "Batch not found"}, status=status.HTTP_404_NOT_FOUND)
