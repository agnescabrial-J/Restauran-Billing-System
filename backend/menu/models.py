from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('STARTER', 'Starter'),
        ('MAIN', 'Main'),
        ('DRINK', 'Drink'),
        ('DESSERT', 'Dessert'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)