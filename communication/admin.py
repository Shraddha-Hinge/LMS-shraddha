from django.contrib import admin
from .models import ChatMessage, Announcement, Notification

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "batch", "content", "timestamp")
    search_fields = ("sender__email", "batch__name")
    list_filter = ("timestamp",)

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("sender", "batch", "title", "timestamp")
    search_fields = ("sender__email", "title")
    list_filter = ("timestamp",)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("user", "message", "is_read", "created_at")
    search_fields = ("user__email",)
    list_filter = ("is_read", "created_at")
