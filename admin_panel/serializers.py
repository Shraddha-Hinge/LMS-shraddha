from rest_framework import serializers
from .models import StaffRole, AdminAction

# Staff Role Serializer
class StaffRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffRole
        fields = "__all__"

# Admin Action Serializer
class AdminActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminAction
        fields = "__all__"
