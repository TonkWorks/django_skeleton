# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20150710_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=144)),
                ('description', models.CharField(max_length=5000)),
                ('location', models.CharField(default='Annapolis Junction, MD', max_length=200)),
                ('link', models.CharField(default='', max_length=1000)),
                ('email', models.CharField(default='', max_length=254)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='clearance',
            field=models.CharField(default='TS//SI', max_length=144),
        ),
        migrations.AlterField(
            model_name='job',
            name='email',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='job',
            name='link',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(default='Annapolis Junction, MD', max_length=200),
        ),
    ]
