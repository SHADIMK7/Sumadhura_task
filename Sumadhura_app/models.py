# models.py
from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=100)
    dc_number = models.CharField(max_length=50)
    po_number = models.CharField(max_length=50)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    checked_out = models.BooleanField(default=False)
    

    def __str__(self):
        return self.vehicle_number

class QualityCheck(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    passed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.vehicle} - {'Passed' if self.passed else 'Failed'}"
