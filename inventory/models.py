from django.db import models

# Create your models here.
from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class DeviceType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    serial_no = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    software_version = models.CharField(max_length=255)

    def __str__(self):
        return self.name
