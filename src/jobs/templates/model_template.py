from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from rest_framework import routers, serializers, viewsets

import datetime
import uuid

from django.db import models
from django.conf import settings
from django.utils import timezone
from tinymce.models import HTMLField


class [[model_name]](models.Model):
[[model_definition]]

# Serializers define the API representation.
class Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = [[model_name]]()
        fields = model._meta.get_all_field_names()

# ViewSets define the view behavior.
class [[model_name]]ViewSet(viewsets.ModelViewSet):
    queryset = [[model_name]].objects.all()
    serializer_class = Serializer