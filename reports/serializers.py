from rest_framework import serializers
from .models import StudentPerformance, PlatformAnalytics

# Student Performance Serializer
class StudentPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPerformance
        fields = "__all__"

# Platform Analytics Serializer
class PlatformAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformAnalytics
        fields = "__all__"
