from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from rest_framework import routers, serializers, viewsets

import datetime
import uuid

from django.db import models
from django.conf import settings
from django.utils import timezone
from tinymce.models import HTMLField


class investment(models.Model):
    company_permalink =  models.CharField(max_length=1000)
    company_name =  models.CharField(max_length=1000)
    company_category_list =  models.CharField(max_length=1000)
    company_market =  models.CharField(max_length=1000)
    company_country_code =  models.CharField(max_length=1000)
    company_state_code =  models.CharField(max_length=1000)
    company_region =  models.CharField(max_length=1000)
    company_city =  models.CharField(max_length=1000)
    investor_permalink =  models.CharField(max_length=1000)
    investor_name =  models.CharField(max_length=1000)
    investor_category_list = models.DateTimeField(null=True)
    investor_market = models.DateTimeField(null=True)
    investor_country_code = models.DateTimeField(null=True)
    investor_state_code = models.DateTimeField(null=True)
    investor_region = models.DateTimeField(null=True)
    investor_city = models.DateTimeField(null=True)
    funding_round_permalink =  models.CharField(max_length=1000)
    funding_round_type =  models.CharField(max_length=1000)
    funding_round_code = models.CharField(max_length=1000)
    funded_at = models.DateTimeField(null=True)
    raised_amount_usd = models.IntegerField(null=True)

# Serializers define the API representation.
class Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = investment()
        fields = model._meta.get_all_field_names()

# ViewSets define the view behavior.
class investmentsViewSet(viewsets.ModelViewSet):
    queryset = investment.objects.all()
    serializer_class = Serializer