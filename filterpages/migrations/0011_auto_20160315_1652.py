# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filterpages', '0010_auto_20160315_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='city_mpg',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='hwy_mpg',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
