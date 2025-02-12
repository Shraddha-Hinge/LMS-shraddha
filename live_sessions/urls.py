from django.urls import path
from .views import ScheduleLiveSessionView, BatchLiveSessionsView, MarkAttendanceView

urlpatterns = [
    path("schedule/", ScheduleLiveSessionView.as_view(), name="schedule-live-session"),
    path("batch/<int:batch_id>/sessions/", BatchLiveSessionsView.as_view(), name="batch-live-sessions"),
    path("attendance/", MarkAttendanceView.as_view(), name="mark-attendance"),
]
