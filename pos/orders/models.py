from django.db import models

# Create your models here.
class order (models.Model):
    serial_number = models.CharField(max_length=200, null=True)
    customer_name = models.CharField(max_length=255, null=True)
    item = models.CharField(max_length=255, null=True)
    quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.customer_name} - {self.item} (x{self.quantity})"