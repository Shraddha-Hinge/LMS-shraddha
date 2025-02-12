from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import SyllabusProgress
from .serializers import SyllabusProgressSerializer
from accounts.permissions import IsStaff

# Unlock Syllabus Topic for a Batch (Only Staff)
class UnlockSyllabusTopicView(generics.UpdateAPIView):
    queryset = SyllabusProgress.objects.all()
    serializer_class = SyllabusProgressSerializer
    permission_classes = [IsAuthenticated, IsStaff]

    def update(self, request, *args, **kwargs):
        syllabus = self.get_object()
        syllabus.is_unlocked = True
        syllabus.save()
        return Response({"message": "Syllabus topic unlocked"}, status=status.HTTP_200_OK)
