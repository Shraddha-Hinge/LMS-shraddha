from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Course, Batch, SyllabusProgress
from .serializers import CourseSerializer, BatchSerializer, SyllabusProgressSerializer
from accounts.permissions import IsStaff, IsAdmin

# Course List & Create View (Only Admins & Staff)
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsStaff | IsAdmin]

# Retrieve, Update, Delete Course (Only Admins)
class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

# Batch List & Create View (Only Admins & Staff)
class BatchListCreateView(generics.ListCreateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    permission_classes = [IsAuthenticated, IsStaff | IsAdmin]

# Retrieve, Update, Delete Batch (Only Admins)
class BatchDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

# List Batches for a Specific Course (For Staff & Students)
class CourseBatchesView(generics.ListAPIView):
    serializer_class = BatchSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        course_id = self.kwargs["course_id"]
        return Batch.objects.filter(course_id=course_id)

# Archive a Course (Only Admins)
class ArchiveCourseView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def update(self, request, *args, **kwargs):
        course = self.get_object()
        course.is_archived = True
        course.save()
        return Response({"message": "Course archived successfully"}, status=status.HTTP_200_OK)
