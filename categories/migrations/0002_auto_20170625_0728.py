# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 07:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_by',
            field=models.CharField(blank=True, default=b'', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 25, 7, 28, 18, 344397, tzinfo=utc), editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='category',
            name='modified_by',
            field=models.CharField(blank=True, default=b'', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 25, 7, 28, 20, 14576, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
