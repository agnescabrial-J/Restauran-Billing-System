from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    table_number = serializers.IntegerField(source='table.id', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'table_number', 'status', 'created_at']