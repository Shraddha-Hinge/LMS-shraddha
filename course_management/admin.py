from django.contrib import admin
from .models import Course, Batch, SyllabusProgress

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "instructor", "is_archived")
    search_fields = ("title", "instructor__email")
    list_filter = ("is_archived",)

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ("name", "course", "tutor", "start_date", "end_date")  
    search_fields = ("name", "course__title", "tutor__email")
    list_filter = ("start_date", "end_date")

@admin.register(SyllabusProgress)
class SyllabusProgressAdmin(admin.ModelAdmin):
    list_display = ("batch", "topic", "is_unlocked")  
    list_filter = ("is_unlocked",)
