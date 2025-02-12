from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import StaffRole, AdminAction
from .serializers import StaffRoleSerializer, AdminActionSerializer
from accounts.models import User
from student_management.models import BatchTransferRequest
from accounts.permissions import IsAdmin

# Create & Manage Staff Roles
class StaffRoleListCreateView(generics.ListCreateAPIView):
    queryset = StaffRole.objects.all()
    serializer_class = StaffRoleSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def perform_create(self, serializer):
        serializer.save()

# Approve or Reject Batch Transfer Requests
class ApproveBatchTransferView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def update(self, request, *args, **kwargs):
        transfer_request = BatchTransferRequest.objects.get(id=kwargs["pk"])
        action = request.data.get("action")

        if action == "approve":
            transfer_request.student.current_batch = transfer_request.new_batch
            transfer_request.student.save()
            transfer_request.status = "approved"
            transfer_request.save()
            return Response({"message": "Batch transfer approved"}, status=status.HTTP_200_OK)

        elif action == "reject":
            transfer_request.status = "rejected"
            transfer_request.save()
            return Response({"message": "Batch transfer rejected"}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)

# View Admin Actions
class AdminActionListView(generics.ListAPIView):
    serializer_class = AdminActionSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def get_queryset(self):
        return AdminAction.objects.all()
