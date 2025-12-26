from django.urls import path
from .views import GenerateBillAPIView, MarkBillPaidAPIView, DownloadBillPDFAPIView

urlpatterns = [
    path('generate/<int:table_id>/', GenerateBillAPIView.as_view()),
    path('pay/<int:bill_id>/', MarkBillPaidAPIView.as_view()),
    path('download/<int:bill_id>/', DownloadBillPDFAPIView.as_view()),
]