# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filterpages', '0021_carmodel_battery'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='motor',
            field=models.CommaSeparatedIntegerField(blank=True, max_length=255),
        ),
    ]
