from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Table

class TableListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tables = Table.objects.all()
        data = [
            {
                "id": table.id,
                "number": table.number,
                "status": table.status
            }
            for table in tables
        ]
        return Response(data)