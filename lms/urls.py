from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("student_management/", include("student_management.urls")),
    path("course_management/", include("course_management.urls")),
    path("resource_hub/", include("resource_hub.urls")),
    path("assessments/", include("assessments.urls")),
    path("communication/", include("communication.urls")),
    path("live_sessions/", include("live_sessions.urls")),
    path("billing/", include("billing.urls")),
    path("notifications/", include("notifications.urls")),
    path("certifications/", include("certifications.urls")),
    path("reports/", include("reports.urls")),
    path("admin_panel/", include("admin_panel.urls")),
]
