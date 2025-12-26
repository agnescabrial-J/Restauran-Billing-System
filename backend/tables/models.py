from django.db import models

class Table(models.Model):
    STATUS_CHOICES = [
        ('AVAILABLE', 'Available'),
        ('OCCUPIED', 'Occupied'),
        ('BILL_REQUESTED', 'Bill Requested'),
        ('CLOSED', 'Closed'),
    ]

    table_number = models.IntegerField(unique=True)
    seating_capacity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='AVAILABLE')

    def __str__(self):
        return f"Table {self.table_number}"