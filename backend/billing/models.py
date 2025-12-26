from django.db import models
from tables.models import Table

class Bill(models.Model):
    STATUS_CHOICES = [
        ('NOT_GENERATED', 'Not Generated'),
        ('PENDING', 'Pending Payment'),
        ('PAID', 'Paid'),
    ]

    table = models.OneToOneField(Table, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
