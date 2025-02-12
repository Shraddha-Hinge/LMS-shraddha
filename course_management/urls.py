from django.urls import path
from .views import (
    CourseListCreateView, CourseDetailView, BatchListCreateView, BatchDetailView,
    CourseBatchesView, ArchiveCourseView
)
from .syllabus_progress import UnlockSyllabusTopicView

urlpatterns = [
    path("courses/", CourseListCreateView.as_view(), name="course-list"),
    path("courses/<int:pk>/", CourseDetailView.as_view(), name="course-detail"),
    path("courses/<int:course_id>/batches/", CourseBatchesView.as_view(), name="course-batches"),
    path("batches/", BatchListCreateView.as_view(), name="batch-list"),
    path("batches/<int:pk>/", BatchDetailView.as_view(), name="batch-detail"),
    path("courses/<int:pk>/archive/", ArchiveCourseView.as_view(), name="archive-course"),
    path("syllabus/<int:pk>/unlock/", UnlockSyllabusTopicView.as_view(), name="unlock-syllabus"),
]
