from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from rest_framework import routers, serializers, viewsets

import datetime
import uuid

from django.db import models
from django.conf import settings
from django.utils import timezone
from tinymce.models import HTMLField

class acquisition(models.Model):
    company_permalink =  models.CharField(max_length=1000)
    company_name =  models.CharField(max_length=1000)
    company_category_list =  models.CharField(max_length=1000)
    company_market =  models.CharField(max_length=1000)
    company_country_code =  models.CharField(max_length=1000)
    company_state_code =  models.CharField(max_length=1000)
    company_region =  models.CharField(max_length=1000)
    company_city =  models.CharField(max_length=1000)
    acquirer_permalink =  models.CharField(max_length=1000)
    acquirer_name =  models.CharField(max_length=1000)
    acquirer_category_list =  models.CharField(max_length=1000)
    acquirer_market =  models.CharField(max_length=1000)
    acquirer_country_code =  models.CharField(max_length=1000)
    acquirer_state_code =  models.CharField(max_length=1000)
    acquirer_region =  models.CharField(max_length=1000)
    acquirer_city =  models.CharField(max_length=1000)
    acquired_at = models.DateTimeField(null=True)
    acquired_month = models.DateTimeField(null=True)
    price_amount = models.IntegerField(null=True)
    price_currency_code =  models.CharField(max_length=1000)

# Serializers define the API representation.
class Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = acquisition
        fields = model._meta.get_all_field_names()
