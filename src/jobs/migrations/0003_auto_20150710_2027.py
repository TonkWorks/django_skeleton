# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20150709_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='clearance',
            field=models.CharField(default='', max_length=144),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(default='Columbia, MD', max_length=200),
            preserve_default=False,
        ),
    ]
