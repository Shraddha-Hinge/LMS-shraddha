from django.contrib import admin
from .models import StaffRole, AdminAction

@admin.register(StaffRole)
class StaffRoleAdmin(admin.ModelAdmin):
    list_display = ("user", "role")
    list_filter = ("role",)
    search_fields = ("user__email",)

@admin.register(AdminAction)
class AdminActionAdmin(admin.ModelAdmin):
    list_display = ("admin", "action", "timestamp")
    search_fields = ("admin__email", "action")
    list_filter = ("timestamp",)
