# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-06 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0017_auto_20160117_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cookie_uuid', models.CharField(max_length=144)),
                ('domain', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='acquisition',
            name='price_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='funding_round_code',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
