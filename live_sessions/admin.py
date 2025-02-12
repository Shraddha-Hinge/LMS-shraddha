from django.contrib import admin
from .models import LiveSession, Attendance

@admin.register(LiveSession)
class LiveSessionAdmin(admin.ModelAdmin):
    list_display = ("title", "batch", "tutor", "scheduled_time")  
    search_fields = ("title", "batch__name", "tutor__email")
    list_filter = ("scheduled_time",)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("student", "session", "joined_at")  
    search_fields = ("student__email", "session__title")
    list_filter = ("joined_at",)
