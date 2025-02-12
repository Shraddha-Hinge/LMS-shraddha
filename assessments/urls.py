from django.urls import path
from .views import (
    TaskListCreateView, TaskDetailView, TaskSubmissionCreateView, QuizSubmissionCreateView
)

urlpatterns = [
    path("tasks/", TaskListCreateView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/submit/", TaskSubmissionCreateView.as_view(), name="task-submit"),
    path("quizzes/submit/", QuizSubmissionCreateView.as_view(), name="quiz-submit"),
]
