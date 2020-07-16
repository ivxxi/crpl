from django.db import models
from driver.models import Location

#Import User method for django
from django.contrib.auth.models import User


class Passenger(models.Model):

    name = models.OneToOneField(User, related_name='rider_profile',on_delete=models.CASCADE)
    bio = models.CharField(max_length=60)
    avatar = models.ImageField(upload_to='ProfilePicture/')
    current_location = models.ForeignKey('driver.Location', related_name='current_location', on_delete=models.CASCADE, null=True)
    pickup_location = models.ForeignKey('driver.Location',related_name='rider_pickup', on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=50)

    
    def __str__(self):
        return self.name
