# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toyrobot_api', '0002_auto_20160312_0519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='robot',
            name='facing',
        ),
        migrations.AddField(
            model_name='direction',
            name='facing',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
