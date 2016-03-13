# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 04:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('x_cord', models.FloatField()),
                ('y_cord', models.FloatField()),
                ('facing', models.FloatField()),
                ('dirs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toyrobot_api.Direction', verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('table_l', models.FloatField()),
                ('table_r', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='robot',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toyrobot_api.Table', verbose_name='name'),
        ),
    ]
