from django.db import models
from django.contrib.auth.models import User


class Driver(models.Model):
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=60)
    avatar = models.ImageField(upload_to='ProfilePicture/')
    vehicle = models.ForeignKey('driver.Car', on_delete=models.CASCADE)
    pickup_location = models.ForeignKey('driver.Location', on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=50)

    
    def __str__(self):
        return self.name

class Car(models.Model):
    car_brand = models.CharField(max_length=50)
    number_plate = models.CharField(max_length=20)

    def __str__(self):
        return self.car_brand

class Location (models.Model):
    location_name = models.CharField(max_length=20)

    def __str__(self):
        return self.location_name

class Category (models.Model):
    pickup_location = models.CharField(max_length=20)
    arrival_destination = models.CharField(max_length=20)

 
    def __str__(self):
        return self.pickup_location

