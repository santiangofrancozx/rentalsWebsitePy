from django.db import models
from django.contrib.auth.models import User  

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
    transmission = models.CharField(max_length=100, default='Automatic')
    air = models.BooleanField(default= False)
    doors = models.IntegerField(default= 4)
    kilometers = models.IntegerField(default=0)
    img = models.ImageField(upload_to='img', default='default_image.jpg')  # upload_to especifica la carpeta donde se guardarán las imágenes

    def __str__(self):
        return self.model
class Reservation(models.Model):
    price_total = models.IntegerField()
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    pickup_date = models.DateField()
    return_date = models.DateField()
    pickup_location = models.CharField(max_length=255)
    

class Comments(models.Model):
    username =  models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    comment =  models.CharField(max_length=255)