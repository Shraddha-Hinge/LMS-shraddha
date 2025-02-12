from course_management.models import Course
from assessments.models import TaskSubmission
from live_sessions.models import Attendance
from billing.models import Payment
from .models import StudentPerformance, PlatformAnalytics

# Generate Student Performance Report
def update_student_performance(student, course):
    total_tasks = course.assessments.count()
    completed_tasks = TaskSubmission.objects.filter(student=student, task__batch__course=course).count()
    
    completion_percentage = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    avg_test_score = TaskSubmission.objects.filter(student=student, task__batch__course=course).aggregate(avg_score=models.Avg("grade"))["avg_score"] or 0
    attendance_rate = Attendance.objects.filter(student=student, session__batch__course=course).count()

    StudentPerformance.objects.update_or_create(
        student=student, course=course,
        defaults={"completion_percentage": completion_percentage, "avg_test_score": avg_test_score, "attendance_rate": attendance_rate}
    )

# Generate Platform-Wide Analytics Report
def update_platform_analytics():
    total_students = User.objects.filter(role="student").count()
    active_courses = Course.objects.filter(is_archived=False).count()
    total_revenue = Payment.objects.filter(status="completed").aggregate(total=models.Sum("amount"))["total"] or 0

    PlatformAnalytics.objects.update_or_create(id=1, defaults={"total_students": total_students, "active_courses": active_courses, "total_revenue": total_revenue})
