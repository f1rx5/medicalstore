from django.db import models
from django.utils import timezone

# Create your models here.
class Medicine(models.Model):
    medicine_name=models.CharField(max_length=30)
    purchase_price=models.CharField(max_length=15)
    quantity=models.CharField(max_length=15)
    selling_price=models.CharField(max_length=15)

