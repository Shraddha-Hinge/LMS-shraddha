from django.contrib import admin
from .models import Task, TaskSubmission, QuizQuestion, QuizSubmission

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "batch", "task_type", "due_date")
    search_fields = ("title", "batch__name")
    list_filter = ("task_type", "due_date")

@admin.register(TaskSubmission)
class TaskSubmissionAdmin(admin.ModelAdmin):
    list_display = ("student", "task", "submitted_at", "grade")
    search_fields = ("student__email", "task__title")
    list_filter = ("submitted_at",)

@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "task", "correct_option")
    search_fields = ("question_text", "task__title")
    list_filter = ("correct_option",)

@admin.register(QuizSubmission)
class QuizSubmissionAdmin(admin.ModelAdmin):
    list_display = ("student", "task", "selected_option", "is_correct")
    search_fields = ("student__email", "task__title")
    list_filter = ("is_correct",)
