from django.db import models
from django.conf import settings

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    CARGO_TYPES = [
        ('fragile', 'Fragile'),
        ('liquid', 'Liquid'),
        ('bulk', 'Bulk'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    description = models.TextField(blank=True)
    cargo_type = models.CharField(max_length=20, choices=CARGO_TYPES)
    weight = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    pickup_address = models.CharField(max_length=255, blank=True)
    delivery_address = models.CharField(max_length=255, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.title}"