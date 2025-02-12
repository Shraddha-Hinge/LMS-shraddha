from django.urls import path
from .views import StaffRoleListCreateView, ApproveBatchTransferView, AdminActionListView

urlpatterns = [
    path("staff-roles/", StaffRoleListCreateView.as_view(), name="staff-roles"),
    path("batch-transfer/<int:pk>/", ApproveBatchTransferView.as_view(), name="approve-batch-transfer"),
    path("admin-actions/", AdminActionListView.as_view(), name="admin-actions"),
]
