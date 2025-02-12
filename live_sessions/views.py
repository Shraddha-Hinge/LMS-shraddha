from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import LiveSession, Attendance
from .serializers import LiveSessionSerializer, AttendanceSerializer
from accounts.permissions import IsStaff, IsStudent
from notifications.models import Notification

# Schedule a Live Session (Only Staff)
class ScheduleLiveSessionView(generics.CreateAPIView):
    queryset = LiveSession.objects.all()
    serializer_class = LiveSessionSerializer
    permission_classes = [IsAuthenticated, IsStaff]

    def perform_create(self, serializer):
        session = serializer.save()
        
        # Notify students about the live session
        batch_students = session.batch.studentprofile_set.all()
        for student in batch_students:
            Notification.objects.create(user=student.student, message=f"New live session scheduled: {session.title}")
        
        return Response({"message": "Live session scheduled successfully"}, status=status.HTTP_201_CREATED)

# List Live Sessions for a Batch (For Students & Staff)
class BatchLiveSessionsView(generics.ListAPIView):
    serializer_class = LiveSessionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LiveSession.objects.filter(batch=self.kwargs["batch_id"])

# Track Attendance (Students Mark Themselves Present)
class MarkAttendanceView(generics.CreateAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated, IsStudent]

    def perform_create(self, serializer):
        session = serializer.validated_data["session"]
        student = self.request.user
        
        # Check if student is part of the batch
        if student.student_profile.current_batch != session.batch:
            return Response({"error": "You are not in this batch"}, status=status.HTTP_403_FORBIDDEN)
        
        serializer.save(student=student)
        return Response({"message": "Attendance marked successfully"}, status=status.HTTP_201_CREATED)
