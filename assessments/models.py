from django.db import models
from accounts.models import User
from course_management.models import Course, Batch

# Task & Assignment Model
class Task(models.Model):
    TASK_TYPES = (
        ("quiz", "Quiz"),
        ("document_submission", "Document Submission"),
        ("qa_submission", "Q/A Submission"),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    task_type = models.CharField(max_length=50, choices=TASK_TYPES)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name="assessment_tasks")  # ✅ Unique related_name 
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.batch.name})"

# Student Submission Model
class TaskSubmission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submissions")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="submissions")
    submitted_file = models.FileField(upload_to="submissions/", null=True, blank=True)
    submitted_text = models.TextField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.FloatField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.email} - {self.task.title}"

# Auto-Graded Quiz Model
class QuizQuestion(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="quiz_questions")
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1, choices=[("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")])

    def __str__(self):
        return f"{self.question_text} ({self.task.title})"

# Quiz Submission Model
class QuizSubmission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quiz_submissions")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="quiz_submissions")
    selected_option = models.CharField(max_length=1, choices=[("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")])
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.email} - {self.task.title}: {self.selected_option}"
