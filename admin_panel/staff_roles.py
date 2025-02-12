from rest_framework.permissions import BasePermission

class IsCourseManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.staff_role.role == "course_manager"

class IsContentManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.staff_role.role == "content_manager"

class IsAnnouncementManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.staff_role.role == "announcement_manager"
