from django.db import models
from tables.models import Table

class Order(models.Model):
    STATUS_CHOICES = (
        ('PLACED', 'Placed'),
        ('IN_KITCHEN', 'In Kitchen'),
        ('SERVED', 'Served'),
    )

    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PLACED')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - Table {self.table.id}"