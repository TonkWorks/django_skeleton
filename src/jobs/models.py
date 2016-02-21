from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from rest_framework import routers, serializers, viewsets

import datetime
import uuid

from django.db import models
from django.conf import settings
from django.utils import timezone
from tinymce.models import HTMLField


class Job(models.Model):
    title = models.CharField(max_length=144)
    description = HTMLField()
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200, default="Annapolis Junction, MD")
    clearance = models.CharField(max_length=144, default="TS//SI", blank=True)
    link = models.CharField(max_length=1000, default="", blank=True)
    email = models.CharField(max_length=254, default="", blank=True)

    pub_date = models.DateTimeField('date published')

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date < now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


# Serializers define the API representation.
class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ('title', 'description', 'company', 'location', 'clearance', 'link', 'email')

# ViewSets define the view behavior.
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer




class SupportToken(models.Model):
    cookie_uuid = models.CharField(max_length=144)
    domain = models.CharField(max_length=1000)

# Serializers define the API representation.
class SupportTokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SupportToken
        fields = ('cookie_uuid', 'domain')

# ViewSets define the view behavior.
class SupportTokenViewSet(viewsets.ModelViewSet):
    queryset = SupportToken.objects.all()
    serializer_class = SupportTokenSerializer




######################


class Event(models.Model):
    title = models.CharField(max_length=144)
    description = HTMLField()
    location = models.CharField(max_length=200, default="Annapolis Junction, MD")
    link = models.CharField(max_length=1000, default="", blank=True)
    date = models.DateTimeField('date of event')

    picture = models.ImageField('Event picture',
                                upload_to='event_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title

# Serializers define the API representation.
class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'description', 'location', 'link', 'date', 'picture')

# ViewSets define the view behavior.
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
