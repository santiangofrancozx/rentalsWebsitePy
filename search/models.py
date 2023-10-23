from django.db import models

# Create your models here.

from django.db import models

class Vehicle(models.Model):
    model = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    year = models.IntegerField()
    vehicle_type = models.CharField(max_length=255)
    availability = models.BooleanField()
    location = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.model
class Reservation(models.Model):
    client_id = models.IntegerField()  # Aquí puedes enlazar con un modelo de cliente si es necesario
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    pickup_date = models.DateField()
    return_date = models.DateField()
    pickup_location = models.CharField(max_length=255)
