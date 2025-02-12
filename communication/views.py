from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import ChatMessage, Announcement, Notification
from .serializers import ChatMessageSerializer, AnnouncementSerializer, NotificationSerializer
from accounts.permissions import IsStudent, IsStaff, IsAdmin

# Send & Retrieve Chat Messages (Students & Staff)
class ChatMessageListCreateView(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    permission_classes = [IsAuthenticated, IsStudent | IsStaff]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

# Create Announcement (Only Staff & Admins)
class AnnouncementCreateView(generics.CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated, IsStaff | IsAdmin]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

# List Announcements (For Students & Staff)
class AnnouncementListView(generics.ListAPIView):
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Announcement.objects.filter(batch=user.student_profile.current_batch) | Announcement.objects.filter(batch=None)

# Send Notification (Admins Only)
class SendNotificationView(generics.CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def perform_create(self, serializer):
        serializer.save()
