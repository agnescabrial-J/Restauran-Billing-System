from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Bill
from .pdf import generate_bill_pdf
from orders.models import Order
from tables.models import Table
from users.permissions import IsCashier


class GenerateBillAPIView(APIView):
    permission_classes = [IsAuthenticated, IsCashier]

    def post(self, request, table_id):
        table = get_object_or_404(Table, id=table_id)
        order = Order.objects.filter(table=table).last()

        if not order:
            return Response({"error": "No order found"}, status=400)

        bill, created = Bill.objects.get_or_create(
            table=table,
            defaults={
                "total_amount": order.total_amount(),
                "status": "PENDING"
            }
        )

        return Response({
            "bill_id": bill.id,
            "total": bill.total_amount,
            "status": bill.status
        })


class MarkBillPaidAPIView(APIView):
    permission_classes = [IsAuthenticated, IsCashier]

    def post(self, request, bill_id):
        bill = get_object_or_404(Bill, id=bill_id)

        bill.status = "PAID"
        bill.save()

        table = bill.table
        table.status = "AVAILABLE"
        table.save()

        return Response({"message": "Bill paid successfully"})


class DownloadBillPDFAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, bill_id):
        bill = get_object_or_404(Bill, id=bill_id)
        return generate_bill_pdf(bill)
