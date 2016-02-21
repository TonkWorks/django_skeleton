# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20150710_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.ImageField(upload_to='event_pics/%Y-%m-%d/', null=True, verbose_name='Event picture', blank=True),
        ),
    ]
