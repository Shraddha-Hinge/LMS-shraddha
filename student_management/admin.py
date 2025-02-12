from django.contrib import admin
from .models import StudentProfile, StudentProgress, BatchTransferRequest

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ("student", "current_batch")  
    search_fields = ("student__email", "current_batch__name")

@admin.register(StudentProgress)
class StudentProgressAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "completed_percentage", "last_updated")
    search_fields = ("student__email", "course__title")
    list_filter = ("last_updated",)

@admin.register(BatchTransferRequest)
class BatchTransferRequestAdmin(admin.ModelAdmin):
    list_display = ("student", "current_batch", "requested_batch", "status")  
    search_fields = ("student__email", "current_batch__name", "requested_batch__name")
    list_filter = ("status",)
