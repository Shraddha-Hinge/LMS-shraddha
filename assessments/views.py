from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task, TaskSubmission, QuizQuestion, QuizSubmission
from .serializers import TaskSerializer, TaskSubmissionSerializer, QuizQuestionSerializer, QuizSubmissionSerializer
from accounts.permissions import IsStaff, IsStudent, IsAdmin

# Create & List Tasks (Only Staff/Admin)
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsStaff | IsAdmin]

# Retrieve, Update, Delete Task (Only Staff/Admin)
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsStaff | IsAdmin]

# Submit Task (Only Students)
class TaskSubmissionCreateView(generics.CreateAPIView):
    serializer_class = TaskSubmissionSerializer
    permission_classes = [IsAuthenticated, IsStudent]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

# Auto-Grade Quiz Submission
class QuizSubmissionCreateView(generics.CreateAPIView):
    serializer_class = QuizSubmissionSerializer
    permission_classes = [IsAuthenticated, IsStudent]

    def create(self, request, *args, **kwargs):
        student = request.user
        task_id = request.data.get("task")
        selected_option = request.data.get("selected_option")

        try:
            task = Task.objects.get(id=task_id)
            correct_answer = QuizQuestion.objects.get(task=task).correct_option

            is_correct = selected_option == correct_answer
            submission = QuizSubmission.objects.create(student=student, task=task, selected_option=selected_option, is_correct=is_correct)

            return Response({"message": "Quiz submitted", "is_correct": is_correct}, status=status.HTTP_201_CREATED)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
