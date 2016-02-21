# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20150710_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_email',
            field=models.CharField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='job_link',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.CharField(max_length=5000),
        ),
    ]
