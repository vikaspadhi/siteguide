from enum import unique
from django.db import models

# Create your models here.
class Vehicle(models.Model):
    slug = models.SlugField(null=True,blank=True,max_length=250)
    vehicle_name = models.CharField(max_length=500)
    speed = models.CharField(max_length=500)
    average_speed = models.CharField(max_length=500)
    engine_status = models.CharField(max_length=500)
    engine_status = models.CharField(max_length=500)
    fuel_level = models.CharField(max_length=500)
    temperature = models.CharField(max_length=500)
    on_off = models.CharField(max_length=500)
    
    
    def __str__(self):
        return  f"{self.vehicle_name}"