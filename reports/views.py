from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import StudentPerformance, PlatformAnalytics
from .serializers import StudentPerformanceSerializer, PlatformAnalyticsSerializer
from accounts.permissions import IsAdmin, IsStaff

# Student Performance Report (For Students & Staff)
class StudentPerformanceReportView(generics.ListAPIView):
    serializer_class = StudentPerformanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == "student":
            return StudentPerformance.objects.filter(student=self.request.user)
        elif self.request.user.role in ["staff", "admin"]:
            return StudentPerformance.objects.all()

# Platform Analytics Report (Admin Only)
class PlatformAnalyticsView(generics.ListAPIView):
    serializer_class = PlatformAnalyticsSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def get_queryset(self):
        return PlatformAnalytics.objects.all()
