from django.contrib import admin
from .models import StudentPerformance, PlatformAnalytics

@admin.register(StudentPerformance)
class StudentPerformanceAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "completion_percentage", "avg_test_score", "attendance_rate")
    search_fields = ("student__email", "course__title")
    list_filter = ("completion_percentage",)

@admin.register(PlatformAnalytics)
class PlatformAnalyticsAdmin(admin.ModelAdmin):
    list_display = ("total_students", "active_courses", "total_revenue", "updated_at")
    list_filter = ("updated_at",)
