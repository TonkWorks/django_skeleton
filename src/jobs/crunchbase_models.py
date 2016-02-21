from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from rest_framework import routers, serializers, viewsets

import datetime
import uuid

from django.db import models
from django.conf import settings
from django.utils import timezone
from tinymce.models import HTMLField


class Company(models.Model):
    permalink = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    homepage_url = models.CharField(max_length=1000)
    market = models.CharField(max_length=1000)
    category_list = models.CharField(max_length=1000)
    funding_total_usd = models.BigIntegerField(null=True)
    status = models.CharField(max_length=144)
    country_code = models.CharField(max_length=144)
    state_code = models.CharField(max_length=144)
    region = models.CharField(max_length=144)
    city = models.CharField(max_length=144)
    funding_rounds = models.IntegerField(null=True)
    founded_at = models.DateTimeField(null=True)
    first_funding_at = models.DateTimeField(null=True)
    last_funding_at = models.DateTimeField(null=True)


# Serializers define the API representation.
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = model._meta.get_all_field_names()

# ViewSets define the view behavior.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer