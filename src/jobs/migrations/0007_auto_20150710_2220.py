# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20150710_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='email',
        ),
        migrations.AddField(
            model_name='event',
            name='picture',
            field=models.ImageField(upload_to='profile_pics/%Y-%m-%d/', null=True, verbose_name='Profile picture', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='link',
            field=models.CharField(default='', max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='clearance',
            field=models.CharField(default='TS//SI', max_length=144, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='email',
            field=models.CharField(default='', max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='link',
            field=models.CharField(default='', max_length=1000, blank=True),
        ),
    ]
