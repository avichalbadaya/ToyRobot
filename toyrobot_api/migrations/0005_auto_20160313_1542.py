# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toyrobot_api', '0004_auto_20160313_0419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='table_l',
        ),
        migrations.RemoveField(
            model_name='table',
            name='table_r',
        ),
        migrations.AddField(
            model_name='table',
            name='table_end',
            field=models.ForeignKey(default=4.0, on_delete=django.db.models.deletion.CASCADE, related_name='table_end', to='toyrobot_api.Coordinates'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='table',
            name='table_start',
            field=models.ForeignKey(default=0.0, on_delete=django.db.models.deletion.CASCADE, related_name='table_start', to='toyrobot_api.Coordinates'),
            preserve_default=False,
        ),
    ]
