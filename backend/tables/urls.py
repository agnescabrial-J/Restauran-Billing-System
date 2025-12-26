from django.urls import path
from .views import TableListAPIView

urlpatterns = [
    path('', TableListAPIView.as_view(), name='list-tables'),
]