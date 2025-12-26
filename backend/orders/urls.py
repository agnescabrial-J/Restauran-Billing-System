from django.urls import path
from .views import CreateOrderAPIView, OrderListAPIView

urlpatterns = [
    path('create/', CreateOrderAPIView.as_view(), name='create-order'),
    path('', OrderListAPIView.as_view(), name='list-orders'),
]