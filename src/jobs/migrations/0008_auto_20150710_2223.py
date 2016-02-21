# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20150710_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 11, 2, 23, 36, 293000, tzinfo=utc), verbose_name='date of event'),
            preserve_default=False,
        ),
    ]
