from rest_framework import serializers
from .models import Course, Batch, SyllabusProgress

# Course Serializer
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

# Batch Serializer
class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = "__all__"

# Syllabus Progress Serializer
class SyllabusProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = SyllabusProgress
        fields = "__all__"
