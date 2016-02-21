# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_auto_20150710_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.ImageField(upload_to='event_pics/%Y-%m-%d/', null=True, verbose_name='Profile picture', blank=True),
        ),
    ]
