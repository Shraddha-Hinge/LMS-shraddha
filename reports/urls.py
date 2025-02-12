from django.urls import path
from .views import StudentPerformanceReportView, PlatformAnalyticsView
from .export import export_student_performance_csv, export_student_performance_pdf

urlpatterns = [
    path("student-performance/", StudentPerformanceReportView.as_view(), name="student-performance-report"),
    path("platform-analytics/", PlatformAnalyticsView.as_view(), name="platform-analytics"),
    path("export/csv/", export_student_performance_csv, name="export-student-performance-csv"),
    path("export/pdf/", export_student_performance_pdf, name="export-student-performance-pdf"),
]
