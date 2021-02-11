from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profile(models.Model):
    # One-to-one relationship to the default user model. 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    name = models.CharField(max_length = 30)
    date_of_birth = models.DateTimeField(auto_now = False)
    
    # TODO: Add preferences as one-to-many field. 
    # preferences = models.OneToManyField()

    def __str__(self):
        return self.name

class Criteria(models.Model):
    criteria = models.CharField(max_length = 100)
    lower_bound = models.FloatField()
    upper_bound = models.FloatField()

class Event(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length = 100)
    
    # Basic location implementation for now
    # TODO: update after team discussion
    location_latitude = models.FloatField()
    location_longitude = models.FloatField()

    description = models.TextField()
    date = models.DateTimeField(auto_now=False)
    
    # TODO: Implement many-to-many relationship for the guests. 
    # guestList

    is_open_to_public = models.BooleanField(default = True)

    def __str__(self):
        return self.name

