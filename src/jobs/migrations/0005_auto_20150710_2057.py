# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20150710_2049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='job_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='job_link',
            new_name='link',
        ),
    ]
