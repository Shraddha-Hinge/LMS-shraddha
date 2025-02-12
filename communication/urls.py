from django.urls import path
from .views import (
    ChatMessageListCreateView, AnnouncementCreateView, AnnouncementListView, SendNotificationView
)

urlpatterns = [
    path("chat/", ChatMessageListCreateView.as_view(), name="chat-messages"),
    path("announcements/create/", AnnouncementCreateView.as_view(), name="create-announcement"),
    path("announcements/", AnnouncementListView.as_view(), name="list-announcements"),
    path("notifications/send/", SendNotificationView.as_view(), name="send-notification"),
]
