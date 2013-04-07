from django.db import models

# Create your models here.
class User(models.Model):
    image_url = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return str(self.id) + ': ' + self.name

class Friend(models.Model):
    user = models.ForeignKey(User)
    friend = models.IntegerField(default=0)
    def __unicode__(self):
        return str(self.user) + ' has friend ' + str(self.friend)

class Business(models.Model):
    yelp_id = models.CharField(max_length=100)
    json_data = models.TextField()
    def __unicode__(self):
        return str(self.id) + ': ' + self.yelp_id

class Event(models.Model):
    business = models.ForeignKey(Business)
    owner = models.ForeignKey(User)
    yelp_id = models.CharField(max_length=100)
    time_created = models.DateTimeField('time created')
    time_ended = models.DateTimeField('time ended')
    def __unicode__(self):
        return str(self.id) + ': ' + str(self.yelp_id)

class Event_Attendee(models.Model):
    event = models.IntegerField(default=0)
    attendee = models.IntegerField(default=0)
    def __unicode__(self):
        return str(self.event) + ' event has guest ' + str(self.attendee)

