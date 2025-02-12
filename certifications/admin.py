from django.contrib import admin
from .models import Certificate

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("certificate_id", "student", "course", "issue_date")
    search_fields = ("student__email", "course__title", "certificate_id")
    list_filter = ("issue_date",)
