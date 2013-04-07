from django.db import models

# Create your models here.
class User(models.Model):
    image_url = models.CharField(max_length=200)
    name = models.CharField(max_length=50)

class Friend(models.Model):
    user = models.ForeignKey(User)
    friend = models.IntegerField(default=0)

class Event(models.Model):
    yelp_id = models.CharField(max_length=100)
    time_created = models.DateTimeField('time created')
    time_ended = models.DateTimeField('time ended')

class Event_Attendee(models.Model):
    event = models.IntegerField(default=0)
    attendee = models.IntegerField(default=0)

class Business(models.Model):
    json_data = models.TextField()
