from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from tables.models import Table
from .models import Order
from users.permissions import IsWaiter


class CreateOrderAPIView(APIView):
    permission_classes = [IsAuthenticated, IsWaiter]

    def post(self, request):
        table = Table.objects.get(id=request.data['table_id'])
        if table.status == 'AVAILABLE':
            table.status = 'OCCUPIED'
            table.save()
        Order.objects.create(table=table)
        return Response({"message": "Order created"})


class OrderListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.all().order_by('-id')
        data = [{"id": o.id, "table": o.table.id, "status": o.status} for o in orders]
        return Response(data)