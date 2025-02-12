from django.urls import path
from .views import CertificateListView, AdminGenerateCertificateView, CertificateDownloadView

urlpatterns = [
    path("", CertificateListView.as_view(), name="list-certificates"),
    path("admin/generate/", AdminGenerateCertificateView.as_view(), name="admin-generate-certificate"),
    path("download/<uuid:certificate_id>/", CertificateDownloadView.as_view(), name="download-certificate"),
]
