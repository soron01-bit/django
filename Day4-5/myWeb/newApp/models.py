from django.db import models
from django.utils import timezone

class product(models.Model):
    PRODUCT_STATUS = (
        ('available', 'Available'),
        ('unavailable', 'Unavailable')
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    status = models.CharField(max_length=20, choices=PRODUCT_STATUS, default='available')
    created_at = models.DateTimeField(default=timezone.now) 