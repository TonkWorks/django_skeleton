from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from rest_framework import routers, serializers, viewsets

import datetime
import uuid

from django.db import models
from django.conf import settings
from django.utils import timezone
from tinymce.models import HTMLField


class addition(models.Model):
    content =  models.CharField(max_length=1000)
    month_str = models.DateTimeField(null=True)
    year_str = models.IntegerField(null=True)
    value = models.IntegerField(null=True)

# Serializers define the API representation.
class Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = addition()
        fields = model._meta.get_all_field_names()

# ViewSets define the view behavior.
class additionsViewSet(viewsets.ModelViewSet):
    queryset = addition.objects.all()
    serializer_class = Serializer